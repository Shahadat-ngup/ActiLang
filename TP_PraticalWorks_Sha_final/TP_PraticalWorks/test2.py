from parser import parse

usecasedg_text = """
actor_list: Patient as P, Nurse,  Doctor inherits Nurse, Recepcionist as R, Admin as A inherits Recepcionist

system HospitalManagementSystem {
	usecase_list: BookAppointment as BA by Patient, RescheduleAppointment as RA, ConductCheckup by Doctor,
	PrescribeMedication as PM, RegisterPatient as RP by R, ProcessPayment as PP by Recepcionist,
	ManageAppointments as MA by A, GenerateReport as GR by A

	package MedicalProcedures {
		ConductCheckup
		PM
	}

	package PatientServices {
		BA
		RA
		RP
	}

	package Administration {
		PP
		MA
		GR
	}

	relationships {
		inc BookAppointment in RegisterPatient
		ext PrescribeMedication of ConductCheckup
		inh RA from BookAppointment
	}
}
"""

plantuml_output = parse(usecasedg_text)
print(plantuml_output)