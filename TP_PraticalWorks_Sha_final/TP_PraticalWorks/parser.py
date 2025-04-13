import ply.yacc as yacc
from lexer import tokens

# Global variables to store parsed data
actors = []
use_cases = []
relationships = []
system_name = ""
packages = {}


def generate_plantuml():
    """Generate PlantUML code from the parsed data and validate references"""

    # This function generates the PlantUML code for the use case diagram
    # We can't use print statements dirctly in the programs
    # because our language allows referecing of actors and use cases
    # either by name or alias while PlantUML requires the use of aliases if they where defined previously
    # So we need to keep track of the aliases and names used in the diagram.
    # Also, the structure of declaration of usecases and packages is different in our language and PlantUML
    # so we need to iterate over the use cases and packages in order to generate a valid PlantUML code.

    plantuml = ["@startuml", "skinparam dpi 100", "left to right direction"]
    participants = set()
    actor_usecase_relationships = []  # Store actor->usecase relationships here

    # We do the validation before generating the diagram
    # Because if something is missing, we want to stop execution
    # and return the error messages
    errors = []

    # Collect declared actor names and aliases, then union them
    # Our language allows use of either the name or alias interchangeably,
    # so we treat both as valid identifiers when resolving references.
    declared_actor_names = {a['name'] for a in actors}
    declared_actor_aliases = {a['alias'] for a in actors if a['alias']}
    all_declared_actors = declared_actor_names.union(declared_actor_aliases)

    # Collect declared use case names and aliases, then union them
    declared_uc_names = {uc['name'] for uc in use_cases}
    declared_uc_aliases = {uc['alias'] for uc in use_cases if uc['alias']}
    all_declared_ucs = declared_uc_names.union(declared_uc_aliases)

    # Validate actors used in use cases
    # In our language, use cases can reference actors before they’re declared,
    # so we validate these references before generating output to avoid PlantUML errors.
    for uc in use_cases:
        if uc['actor']:
            if uc['actor'] not in all_declared_actors:
                errors.append(
                    f"[ERROR]: Actor '{uc['actor']}' used in use case '{uc['name']}' is not declared.")

    # Validate use case references in packages
    for pkg_name, uc_refs in packages.items():
        for ref in uc_refs:
            if ref not in all_declared_ucs:
                errors.append(
                    f"[ERROR]: Use case '{ref}' in package '{pkg_name}' is not declared.")

    # Validate use case references in relationships
    # Similar to packages, relationships must refer to declared use cases.
    for source, _, target in relationships:
        if source not in all_declared_ucs:
            errors.append(
                f"[ERROR]: Use case '{source}' in relationship is not declared.")
        if target not in all_declared_ucs:
            errors.append(
                f"[ERROR]: Use case '{target}' in relationship is not declared.")

    # Stop execution and return error messages if any issues found
    if errors:
        return "\n".join(errors)

    # Main Diagram Generation Logic

    # Process actors
    for actor in actors:
        # If the actor has an alias, we declare it here using PlantUML's alias syntax.
        # This is necessary because once an alias is declared, PlantUML requires it to be used for any future reference.
        # Our language allows use of either the name or alias later, so we must define both linkages early.
        if actor['alias']:
            plantuml.append(f"actor {actor['name']} as {actor['alias']}")
            display_name = actor['alias']
        else:
            plantuml.append(f"actor {actor['name']}")
            display_name = actor['name']

        participants.add(display_name)
        # Check if the actor inherits from another actor
        # If it does, we add the inheritance relationship to the diagram
        # We use the name of the parent actor in the diagram
        if actor['inherits']:
            parent_display = next(
                (a['alias'] or a['name'] for a in actors if a['name'] == actor['inherits']), actor['inherits'])
            plantuml.append(f"{display_name} -|> {parent_display}")

    # Process system name if provided
    if system_name:
        plantuml.append(f"rectangle {system_name} {{")

    # Collect all use case references inside packages (by name or alias)
    # so we can skip them in the global scope and avoid duplicate declarations.

    pkg_uc_refs = {ref for pkg_ucs in packages.values() for ref in pkg_ucs}

    # Process use cases not referenced in any package (by name or alias)

    for uc in use_cases:
        # Check if the use case has an alias or not
        # If it does, we use the alias in the diagram
        uc_alias = uc['alias'] if uc['alias'] else uc['name']
        uc_names = {uc['name']}
        if uc['alias']:
            uc_names.add(uc['alias'])

        # If the use case is not referenced in any package, we add it to the diagram
        # We also check if the use case has an actor or not
        if not uc_names & pkg_uc_refs:
            if uc['alias']:
                plantuml.append(f'    usecase {uc["name"]} as {uc["alias"]}')
            else:
                plantuml.append(f'    usecase {uc["name"]}')
            participants.add(uc_alias)
            if uc['actor']:
                actor_display = next(
                    (a['alias'] or a['name'] for a in actors if a['name'] == uc['actor']), uc['actor'])
                actor_usecase_relationships.append(
                    f"    {actor_display} --> {uc_alias}")

    # Process packages
    # Each package is a separate namespace for use cases
    # We add the package name to the diagram and then add the use cases inside it
    # We also check if the use case has an actor or not
    # If it does, we add the actor to the diagram
    for pkg_name, uc_refs in packages.items():
        plantuml.append(f"    package {pkg_name} {{")
        for ref in uc_refs:
            for uc in use_cases:
                uc_alias = uc['alias'] if uc['alias'] else uc['name']
                if ref == uc['name'] or (uc['alias'] and ref == uc['alias']):
                    if uc['alias']:
                        plantuml.append(
                            f'        usecase {uc["name"]} as {uc["alias"]}')
                    else:
                        plantuml.append(f'        usecase {uc["name"]}')
                    participants.add(uc_alias)
                    if uc['actor']:
                        actor_display = next(
                            (a['alias'] or a['name'] for a in actors if a['name'] == uc['actor']), uc['actor'])
                        if actor_display not in participants:
                            if any(a['alias'] == actor_display for a in actors if a['alias']):
                                plantuml.append(
                                    f"actor {next(a['name'] for a in actors if a['alias'] == actor_display)} as {actor_display}")
                            else:
                                plantuml.append(f"actor {actor_display}")
                            participants.add(actor_display)
                        actor_usecase_relationships.append(
                            f"    {actor_display} --> {uc_alias}")
                    break
        plantuml.append("    }")

    # Add actor->usecase relationships
    # We add the relationships to the diagram
    plantuml.extend(actor_usecase_relationships)

    # Process relationships (extend/include/inherit)
    # We add the relationships to the diagram
    for source, rel_type, target in relationships:
        source_display = None
        for uc in use_cases:
            if uc['name'] == source or (uc['alias'] and uc['alias'] == source):
                source_display = uc['alias'] if uc['alias'] else uc['name']
                break
        if not source_display:
            source_display = source

        target_display = None
        for uc in use_cases:
            if uc['name'] == target or (uc['alias'] and uc['alias'] == target):
                target_display = uc['alias'] if uc['alias'] else uc['name']
                break
        if not target_display:
            target_display = target

        if rel_type == '<<extend>>':
            plantuml.append(
                f"    {source_display} ..> {target_display} : <<extend>>")
        elif rel_type == '<<include>>':
            plantuml.append(
                f"    {source_display} ..> {target_display} : <<include>>")
        elif rel_type == '--|>':
            plantuml.append(f"    {source_display} --|> {target_display}")

    if system_name:
        plantuml.append("}")

    plantuml.append("@enduml")
    return "\n".join(plantuml)


def p_diagram(p):
    '''diagram : actor_decls system_decl'''
    p[0] = {'actors': p[1], 'system': p[2]}
    # This is the root production rule that combines actor declarations and system definition
    # p[1] contains the list of actors from actor_decls
    # p[2] contains the system definition (name and content) from system_decl


def p_actor_decls(p):
    '''actor_decls : actor_decls actor_decl
                  | actor_decl'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]
    # Handles one or more actor declarations by building a list
    # For multiple declarations (first production), concatenate lists
    # For single declaration (second production), create a new list


def p_actor_decl(p):
    '''actor_decl : ACTOR IDENTIFIER
                 | ACTOR IDENTIFIER AS IDENTIFIER
                 | ACTOR IDENTIFIER INHERITS IDENTIFIER
                 | ACTOR IDENTIFIER AS IDENTIFIER INHERITS IDENTIFIER
                 | ACTOR_LIST COLON actor_items'''
    # Handles all forms of actor declarations:
    # - Simple actor (name only)
    # - Actor with alias
    # - Actor with inheritance
    # - Actor with both alias and inheritance
    # - Actor list (comma-separated actors with optional aliases/inheritance)
    if p[1].lower() == 'actor_list':
        # Add all actors from the list to global actors
        for actor in p[3]:
            # We store parsed actors globally because they are needed during the PlantUML generation phase,
            # where references between use cases, packages, and actors are resolved.
            actors.append(actor)
        p[0] = p[3]
    else:
        actor = {'name': p[2], 'alias': None, 'inherits': None}
        if len(p) >= 4:
            if p[3].lower() == 'as':
                actor['alias'] = p[4]
                if len(p) > 5 and p[5].lower() == 'inherits':
                    actor['inherits'] = p[6]
            elif p[3].lower() == 'inherits':
                actor['inherits'] = p[4]
        actors.append(actor)
        p[0] = [actor]


def p_actor_items(p):
    '''actor_items : actor_items COMMA actor_item
                  | actor_item'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]
    # Handles comma-separated list of actors in an actor_list declaration
    # Builds a list by either appending to existing list (first production)
    # or creating new list (second production)


def p_actor_item(p):
    '''actor_item : IDENTIFIER
                 | IDENTIFIER AS IDENTIFIER
                 | IDENTIFIER INHERITS IDENTIFIER
                 | IDENTIFIER AS IDENTIFIER INHERITS IDENTIFIER'''
    # Handles individual actor items within an actor_list
    # Supports same variations as actor_decl but without the ACTOR keyword
    actor = {'name': p[1], 'alias': None, 'inherits': None}
    if len(p) >= 3:
        if p[2].lower() == 'as':
            actor['alias'] = p[3]
            if len(p) > 4 and p[4].lower() == 'inherits':
                actor['inherits'] = p[5]
        elif p[2].lower() == 'inherits':
            actor['inherits'] = p[3]
    p[0] = actor


def p_system_decl(p):
    '''system_decl : SYSTEM IDENTIFIER LBRACE system_content RBRACE
                  | empty'''
    # Handles system declaration with name and content (use cases, packages, relationships)
    # or empty declaration (second production)
    if len(p) > 2:
        # We store parsed actors globally because they are needed during the PlantUML generation phase.
        global system_name
        system_name = p[2]
        p[0] = {'name': p[2], 'content': p[4]}


def p_system_content(p):
    '''system_content : usecase_decls package_decls relationship_decl'''
    # Combines all components that can appear inside a system declaration
    # p[1] contains use case declarations
    # p[2] contains package declarations
    # p[3] contains relationship declarations
    p[0] = {
        'use_cases': p[1],
        'packages': p[2],
        'relationships': p[3]
    }


def p_usecase_decls(p):
    '''usecase_decls : usecase_decls usecase_decl
                    | usecase_decl
                    | USECASE_LIST COLON usecase_items'''
    # Handles one or more use case declarations or a use case list
    # First two productions handle individual declarations (building a list)
    # Third production handles the USECASE_LIST shorthand syntax
    if len(p) == 4 and p[1].lower() == 'usecase_list':
        # Add all use cases from the list to global use_cases
        for uc in p[3]:
            # We store parsed use cases globally because they are needed during the PlantUML generation phase,
            # where references between use cases, packages, and actors are resolved.
            use_cases.append(uc)
        p[0] = p[3]
    elif len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_usecase_items(p):
    '''usecase_items : usecase_items COMMA usecase_item
                    | usecase_item'''
    # Handles comma-separated list of use cases in a USECASE_LIST
    # Similar to actor_items but for use cases
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_usecase_item(p):
    '''usecase_item : IDENTIFIER
                   | IDENTIFIER AS IDENTIFIER
                   | IDENTIFIER BY IDENTIFIER
                   | IDENTIFIER AS IDENTIFIER BY IDENTIFIER'''
    # Handles individual use case items within a USECASE_LIST
    # Supports name only, name with alias, name with actor, or all three
    usecase = {'name': p[1], 'alias': None, 'actor': None}
    if len(p) >= 3:
        if p[2].lower() == 'as':
            usecase['alias'] = p[3]
            if len(p) > 4 and p[4].lower() == 'by':
                usecase['actor'] = p[5]
        elif p[2].lower() == 'by':
            usecase['actor'] = p[3]
    p[0] = usecase


def p_usecase_decl(p):
    '''usecase_decl : USECASE IDENTIFIER
                   | USECASE IDENTIFIER AS IDENTIFIER
                   | USECASE IDENTIFIER BY IDENTIFIER
                   | USECASE IDENTIFIER AS IDENTIFIER BY IDENTIFIER'''
    # Handles individual use case declarations (same variations as usecase_item but with USECASE keyword)
    usecase = {'name': p[2], 'alias': None, 'actor': None}
    if len(p) >= 4:
        if p[3].lower() == 'as':
            usecase['alias'] = p[4]
            if len(p) > 5 and p[5].lower() == 'by':
                usecase['actor'] = p[6]
        elif p[3].lower() == 'by':
            usecase['actor'] = p[4]
    use_cases.append(usecase)
    p[0] = usecase


def p_package_decls(p):
    '''package_decls : package_decls package_decl
                    | package_decl'''
    # Handles one or more package declarations by building a dictionary
    # Keys are package names, values are lists of use case references
    if len(p) == 3:
        p[1].update(p[2])
        p[0] = p[1]
    else:
        p[0] = p[1]


def p_package_decl(p):
    '''package_decl : PACKAGE IDENTIFIER LBRACE usecase_refs RBRACE'''
    # Handles a single package declaration with name and contained use case references
    # We store parsed packages globally because they are needed during the PlantUML generation phase,
    # where references between use cases and packages are resolved.
    packages[p[2]] = p[4]
    p[0] = {p[2]: p[4]}


def p_usecase_refs(p):
    '''usecase_refs : usecase_refs usecase_ref
                   | usecase_ref'''
    # Handles one or more use case references within a package
    # Builds a list of references (by name or alias)
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_usecase_ref(p):
    '''usecase_ref : IDENTIFIER'''
    # Handles a single use case reference (by name or alias)
    p[0] = p[1]


def p_relationship_decl(p):
    '''relationship_decl : RELATIONSHIPS LBRACE relationship_list RBRACE
                        | empty'''
    # Handles relationship declarations block or empty declaration
    # Returns the list of relationships or empty list
    p[0] = p[3] if len(p) > 2 else []


def p_relationship_list(p):
    '''relationship_list : relationship_list relationship
                        | relationship'''
    # Handles one or more relationship declarations within a relationships block
    # Builds a list of relationships
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_relationship(p):
    '''relationship : EXT IDENTIFIER OF IDENTIFIER
                   | INC IDENTIFIER IN IDENTIFIER
                   | INH IDENTIFIER FROM IDENTIFIER'''
    # Handles individual relationship declarations of three types:
    # EXT = extend, INC = include, INH = inherit
    # Creates appropriate PlantUML relationship syntax
    rel_type = {
        'ext': '<<extend>>',
        'inc': '<<include>>',
        'inh': '--|>'
    }[p[1].lower()]
    # We add the relationship to the global relationships list
    # This is necessary because we need to resolve references between use cases
    # before generating the PlantUML code.
    relationships.append((p[2], rel_type, p[4]))
    p[0] = (p[2], rel_type, p[4])


def p_empty(p):
    'empty :'
    # Handles empty productions (epsilon in grammar terms)
    p[0] = None


def p_error(p):
    if p:
        print(
            f"Syntax error at token {p.type}, value: '{p.value}', line: {p.lineno}")
    else:
        print("Syntax error: Unexpected end of input")


 # Error handling function called by PLY when syntax errors occur
parser = yacc.yacc()


def parse(input_text):
    # Main entry point for parsing input text and generating PlantUML
    global actors, use_cases, relationships, system_name, packages
    # Reset global variables for each parse run to prevent residual data from previous diagrams.
    # Since parsing and diagram generation are tightly coupled,
    # keeping global state clean is critical to correctness.
    actors = []
    use_cases = []
    relationships = []
    system_name = ""
    packages = {}
    parser.parse(input_text)
    return generate_plantuml()
