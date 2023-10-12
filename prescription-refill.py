import tkinter
import tkinter.messagebox as mb

HEALTH_INSURANCE_DISC = 0.10
PRESCRIPTION_COST = 50
SALES_TAX = 0.07

patient_database = {'Lewis Kennedy': ['Spironolactone'],
                    'Christine Redfield': ['Oxycodone'],
                    'Jill Christmas': ['Hydrocodone'],
                    'Abbie Wong': ['Diflucan'],
                    'Alice Aberdeen': ['Amoxicillin']}


Health_coverage = ['Lewis Kennedy', 'Abbie Wong', 'Jill Christmas']
class MYGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Refill Prescriptions')
        self.main_window.geometry('300x250')

        # frames
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)

        # Program greeting
        self.welcome_message1 = tkinter.Label(self.frame1, text="Welcome to Dr. Magic's Prescription Service!")
        self.welcome_message2 = tkinter.Label(self.frame1, text='Refilling prescriptions like magic since 2023!')
        self.welcome_message1.pack()
        self.welcome_message2.pack()

        # Get patient name
        self.patient_name = tkinter.Label(self.frame2, text="Please enter the patient's name: ")
        self.patient_entry = tkinter.Entry(self.frame2, width=25)
        self.patient_name.pack(side='left')
        self.patient_entry.pack()

        # Search button to look for patients
        self.patient_lookup = tkinter.Button(self.frame3, text='Search', command=self.patient_lookup_button)
        self.patient_lookup.pack(side='left')
    
        # This will hold the value for the patient's name
        self.patient_label = tkinter.Label(self.frame4, text='Patient Name: ')
        self.patient_value = tkinter.StringVar()
        self.name_of_patient = tkinter.Label(self.frame4, textvariable=self.patient_value)
        self.patient_value.set('********')
        self.patient_label.pack(side='left')
        self.name_of_patient.pack(side='left')

        # This will hold the value for the prescription name
        self.prescription_label = tkinter.Label(self.frame5, text='Prescription Name: ')
        self.prescription_name = tkinter.StringVar()
        self.name_of_prescription = tkinter.Label(self.frame5, textvariable=self.prescription_name)
        self.prescription_name.set('********')
        self.prescription_label.pack(side='left')
        self.name_of_prescription.pack(side='left')

        # First line of text used for directions and information
        self.text_label1 = tkinter.Label(self.frame6)
        self.text_line1 = tkinter.StringVar()
        self.text1 = tkinter.Label(self.frame6, textvariable=self.text_line1)
        self.text_line1.set('')
        self.text_label1.pack(side='left')
        self.text1.pack(side='left')

        # Second line of text used to display total cost of prescription for patient
        self.text_label2 = tkinter.Label(self.frame7)
        self.text_line2 = tkinter.StringVar()
        self.text2 = tkinter.Label(self.frame7, textvariable=self.text_line2)
        self.text_line2.set('')
        self.text_label2.pack(side='left')
        self.text2.pack(side='left')

        # Refill prescription button function is used to calculate how much a patient owes
        self.prescription_button = tkinter.Button(self.frame8, text='Refill', command=self.refill_prescription_button)
        self.prescription_button.pack(side='left')

        # Exits the program
        self.quit_button = tkinter.Button(self.frame8, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()

        tkinter.mainloop()

    # search button function is used to check if patient is in the database
    # and what their prescriptions are
    def patient_lookup_button(self):
        self.patient_input = (self.patient_entry.get()) 
        self.text_line2.set('')
        if self.patient_input in patient_database:
            mb.showinfo('Search Complete', 'Patient Found!')
            self.patient_value.set(self.patient_input)
            if self.patient_input == 'Lewis Kennedy':
                self.prescription_name.set(patient_database['Lewis Kennedy'])
                self.text_line1.set('Patient and prescription have been found. Please click the refill button.')
            elif self.patient_input == 'Abbie Wong':
                self.prescription_name.set(patient_database['Abbie Wong'])
                self.text_line1.set('Patient and prescription have been found. Please click the refill button.')
            elif self.patient_input == 'Christine Redfield':
                self.prescription_name.set(patient_database['Christine Redfield'])
                self.text_line1.set('Patient and prescription have been found. Please click the refill button.')
            elif self.patient_input == 'Jill Christmas':
                self.prescription_name.set(patient_database['Jill Christmas'])
                self.text_line1.set('Patient and prescription have been found. Please click the refill button.')
            elif self.patient_input == 'Alice Aberdeen':
                self.prescription_name.set(patient_database['Alice Aberdeen'])
                self.text_line1.set('Patient and prescription have been found. Please click the refill button.')
        else:
            mb.showerror('404','Patient not in database.') # Displays error window and message

    # Refill prescription function contains the calculations for finding 
    # cost for prescriptions 
    def refill_prescription_button(self):
        try:
            if self.patient_input in Health_coverage:
                self.text_line1.set('Patient has health insurance. Prescription at reduced price.')
                covered_patient_discount = PRESCRIPTION_COST * HEALTH_INSURANCE_DISC
                sales_tax = covered_patient_discount * SALES_TAX
                prescription_total = covered_patient_discount + sales_tax
                self.text_line2.set(f'Prescription: for patient {self.patient_input} has been filled!\n\tThe total cost is ${prescription_total:.2f}')
                mb.showinfo('Refill Complete', 'Prescription Successfully Refilled! '
                            'Please click the quit button to exit the program if you are done.')
            else:
                self.text_line1.set('Patient has no health insurance. Charge full price.')
                prescription_total = (PRESCRIPTION_COST * SALES_TAX) + PRESCRIPTION_COST
                self.text_line2.set(f'Prescription: for patient {self.patient_input} has been filled! \n\tThe total cost is ${prescription_total:.2f}')
                mb.showinfo('Refill Complete', 'Prescription Successfully Refilled! '
                            'Please click the quit button to exit the program if you are done.')
        except ValueError:
            mb.showerror('Error,' 'Invalid entry. Try again.') # Displays error window and message


my_gui = MYGUI()