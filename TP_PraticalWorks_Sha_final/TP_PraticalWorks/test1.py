from parser import parse

usecasedg_text = """
actor Patient as P
actor Nurse
actor Doctor inherits Nurse
actor Recepcionist as R 
actor Admin as A inherits Recepcionist

system HospitalManagementSystem {
	usecase BookAppointment as BA by Patient
	usecase RescheduleAppointment as RA
	usecase ConductCheckup by Doctor
	usecase PrescribeMedication as PM
	usecase RegisterPatient as RP by R
	usecase ProcessPayment as PP by Recepcionist
	usecase ManageAppointments as MA by A 
	usecase GenerateReport as GR by A

	package MedicalProcedures {
		ConductCheckup
		PM
	}

	package PatientServices {
		BA
		RescheduleAppointment
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