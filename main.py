class Patient:
    def __init__(self,ismi,age):
        self.ismi=ismi
        self.age=age
class Doctor:
    def __init__(self,ismi,specialty):
        self.ismi=ismi
        self.specialty=specialty
class Appointment :
    def __init__(self,date,patient,doctor ):
        self.date=date
        self.patient=patient
        self.doctor=doctor
    def show_appointment(self):
        print("Sana:" + self.date)
        print("Bemor:" + self.patient.ismi,","+ str(self.patient.age) +"" + " yosh")
        print( "Shifokor:" + " "+self.doctor.ismi,",", self.doctor.specialty)

bemor1=Patient("Laylo",30)
doctor1=Doctor("Alijon","stamatalog")
bemor2=Patient("Bahodir",25)
doctor2=Doctor("Ali","koz shifokori")
bemor3=Patient("Ali",22)
doctor3=Doctor("Bohodir","yurak duhtri")
appointment1=Appointment("2025-05-25",bemor1,doctor1)
appointment2=Appointment("2026-10-5",bemor2,doctor2
                         )

appointment1.show_appointment()

appointment2.show_appointment()


