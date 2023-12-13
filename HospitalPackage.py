from tkinter import*
from tkinter import messagebox

from itertools import count, cycle
import csv
from PIL import Image, ImageTk
from tkcalendar import *
import os
import sys




PFirstname=''
PLastname=''
PNationalCode=''
PPostalCode=''
PAddress=''
Ptelphone=''
Psexuality=''
DFirstname=''
DLastname=''
DNationalCode=''
DPostalCode=''
DAddress=''
Dtelphone=''
Dsexuality=''
RecordFileNo=''

HospitalizationDate=''
DischargeDate=''
NextVisitDate=''
Description=''
PPrepayment=0
HospitalCost=0
InsuranceShare=0
RemainingCost=0
PreviousRemainder=0
Salary=0
RemainderSalary=0
Pdoctor=''
PdoctorNC=''
PupdateData=False


class mainwindow:
    def __init__(mainwin,root):
        mainwin.root=root
        mainwin.root.title("Sina Hospital Package developed by Goharshadi")
        mainwin.root.geometry("1550x800")
        mainwin.root.config(bg="steel blue")
    

  
                 
class loginwindow(mainwindow):
    
       
    def __init__(mainwin,root,rootlogin):        
        super().__init__(root)
        mainwin.rootlogin=rootlogin
        mainwin.rootlogin.title("Sina Hospital User login")
        mainwin.rootlogin.geometry("300x200")
        mainwin.rootlogin.config(bg="yellow")
        
        def Padd_data():
            
            PNC=mainwin.PtxtNC.get()
            P_CSV_FILE = 'Patients.csv'


            with open(P_CSV_FILE, 'r') as fP:
                reader = csv.reader(fP)
                for Prow in reader:
                    if Prow!=[] and Prow[0]==PNC:
                        messagebox.showerror("Error: the patient NC is exist", "Please correct The national code or if you are sure update data")
                        return
                

            PPrepayment=int(mainwin.PtxtPrepayment.get())
            HospitalCost=int(mainwin.PtxtHospitalCost.get())
            InsuranceShare=int(mainwin.PtxtInsuranceShare.get())
            RemainingCost=HospitalCost-PPrepayment-InsuranceShare
            
            mainwin.PtxtRemainingCost.delete(0,END)
            mainwin.PtxtRemainingCost.insert(0,RemainingCost)
            sex=Psexuality.get()
            d1=mainwin.PcalHospitalizationDate.get()
            d2=mainwin.PcalDischargeDate.get()
            d3=mainwin.PcalNextVisitDate.get()
              
            if sex=='Man' :
                sx='Mr.'
            else :
                sx='Ms.'
                
            PD=mainwin.Pdoctor.get()
            PDNC=mainwin.PdoctorNC.get()
            
            D_CSV_FILE = 'Doctors.csv'
            with open(D_CSV_FILE, 'r') as fD:
                Dreader = csv.reader(fD)
                for Drow in Dreader:
                        if PDNC==Drow[0]:
                            mainwin.DtxtNC.delete(0,END)
                            mainwin.DtxtNC.insert(0,Drow[0])
                            mainwin.DtxtFn.delete(0,END)
                            mainwin.DtxtFn.insert(0,Drow[1])                                                
                            mainwin.DtxtLn.delete(0,END)
                            mainwin.DtxtLn.insert(0,Drow[2])
                            mainwin.DtxtCP.delete(0,END)
                            mainwin.DtxtCP.insert(0,Drow[3])
                            mainwin.DtxtAdr.delete(0,END)
                            mainwin.DtxtAdr.insert(0,Drow[4])
                            mainwin.DtxtTel.delete(0,END)
                            mainwin.DtxtTel.insert(0,Drow[5])
                            Dsexuality.set(value=Drow[6]) 
                            mainwin.DtxtPreviousRemainder.delete(0,END)
                            mainwin.DtxtPreviousRemainder.insert(0,Drow[7])                      
                            mainwin.DtxtSalary.delete(0,END)
                            mainwin.DtxtSalary.insert(0,Drow[8]) 
                            mainwin.DtxtRemainderSalary.delete(0,END)
                            mainwin.DtxtRemainderSalary.insert(0,Drow[9]) 
                            break
                        else:
                            messagebox.showerror("Error Inputing Data","Please correct The treating doctor national code or add the treating doctor to the doctors database")                         
                        
            
            # Open the CSV file for writing
            with open("Patients.csv", mode="a", newline="") as csv_file:

                csv_writer = csv.writer(csv_file)

                csv_writer.writerow([mainwin.PtxtNC.get(),mainwin.PtxtFn.get(),mainwin.PtxtLn.get(),mainwin.PtxtCP.get(),mainwin.PtxtAdr.get(),mainwin.PtxtTel.get(),sex,mainwin.PtxtRFN.get(),PD,PDNC,d1,d2,d3,mainwin.PtxtDescription.get(),PPrepayment,HospitalCost,InsuranceShare,RemainingCost])

            
            
            PShowInf.delete(0,END)
            PShowInf.insert(0,(sx ,mainwin.PtxtFn.get(),mainwin.PtxtLn.get()))
            PShowInf.insert(1,('NationalCode:',mainwin.PtxtNC.get()))
            PShowInf.insert(2,('Tel:',mainwin.PtxtTel.get()))  
            PShowInf.insert(3,('FileNumber:',mainwin.PtxtRFN.get()))
            PShowInf.insert(4,('TreatingDoctor:',PD,'NationalCode:',PDNC))
            PShowInf.insert(5,('HospitalizationDate:',d1))
            PShowInf.insert(6,('DischargeDate:',d2)) 
            PShowInf.insert(7,('NextVisitDay:',d3))  
            PShowInf.insert(8,('Description:',mainwin.PtxtDescription.get()))
            PShowInf.insert(9,('Prepayment=',PPrepayment))
            PShowInf.insert(10,('HospitalCost=',HospitalCost,'InsuranceShare=',InsuranceShare))  
            PShowInf.insert(11,('RemainingCost=',RemainingCost))                     
            PShowInf.insert(12,('Address:',mainwin.PtxtAdr.get(),'PostalCode:',mainwin.PtxtCP.get()))
        

        def Dadd_data():

            DNC=mainwin.DtxtNC.get()
            # D_CSV_FILE = 'Doctors.csv'

            # with open(D_CSV_FILE, 'r') as fD:
            #     Dreader = csv.reader(fD)
            #     for Drow in Dreader:
            #         if DNC==Drow[0]:
                        
            #             messagebox.showerror("The national code of the doctor is exist on the doctors database", "Please correct The national code or if you are sure, update data")
            #             return

            
            PreviousRemainder=int(mainwin.DtxtPreviousRemainder.get())
            Salary=int(mainwin.DtxtSalary.get())
            RemainderSalary=Salary+PreviousRemainder

            mainwin.DtxtRemainderSalary.delete(0,END)
            mainwin.DtxtRemainderSalary.insert(0,RemainderSalary)
            Dsex=Dsexuality.get()
              
            if Dsex=='Man' :
                Dsx='Mr.'
            else :
                Dsx='Ms.'

            
            # Open the CSV file for writing
            with open("Doctors.csv", mode="a", newline="\n") as csv_fileD:
                csv_writerD = csv.writer(csv_fileD)

                csv_writerD.writerow([mainwin.DtxtNC.get(),mainwin.DtxtFn.get(),mainwin.DtxtLn.get(),mainwin.DtxtCP.get(),mainwin.DtxtAdr.get(),mainwin.DtxtTel.get(),Dsex,PreviousRemainder,Salary,RemainderSalary])

            
            DShowInf.delete(0,END)
            DShowInf.insert(0,(Dsx ,mainwin.DtxtFn.get(),mainwin.DtxtLn.get()))
            DShowInf.insert(1,('NationalCode:',mainwin.DtxtNC.get()))
            DShowInf.insert(2,('Tel:',mainwin.DtxtTel.get()))  
            DShowInf.insert(9,('PreviousRemainder=',PreviousRemainder))
            DShowInf.insert(10,('Salary=',Salary))  
            DShowInf.insert(11,('RemainderSalary=',RemainderSalary))                     
            DShowInf.insert(12,('Address:',mainwin.DtxtAdr.get(),'PostalCode:',mainwin.DtxtCP.get()))
        

        def PShow_inf():
            
            PNC=mainwin.PtxtNC.get()

            P_CSV_FILE = 'Patients.csv'
            

            with open(P_CSV_FILE, 'r') as fP:
                reader = csv.reader(fP)
                pat=False
                for Prow in reader:
                    
                    if Prow!=[] and Prow[0]==PNC :
                        pat=True
                        PDNC=Prow[9]
                        mainwin.PtxtFn.delete(0,END)
                        mainwin.PtxtFn.insert(0,Prow[1])
                        mainwin.PtxtLn.delete(0,END)
                        mainwin.PtxtLn.insert(0,Prow[2])
                        mainwin.PtxtCP.delete(0,END)
                        mainwin.PtxtCP.insert(0,Prow[3])
                        mainwin.PtxtAdr.delete(0,END)
                        mainwin.PtxtAdr.insert(0,Prow[4])
                        mainwin.PtxtTel.delete(0,END)
                        mainwin.PtxtTel.insert(0,Prow[5])
                        mainwin.PtxtRFN.delete(0,END)
                        mainwin.PtxtRFN.insert(0,Prow[7])
                        mainwin.Pdoctor.delete(0,END)
                        mainwin.Pdoctor.insert(0,Prow[8])
                        mainwin.PdoctorNC.delete(0,END)
                        mainwin.PdoctorNC.insert(0,PDNC)
                        mainwin.PcalHospitalizationDate.delete(0,END)
                        mainwin.PcalHospitalizationDate.insert(0,Prow[10])
                        mainwin.PcalDischargeDate.delete(0,END)
                        mainwin.PcalDischargeDate.insert(0,Prow[11])
                        mainwin.PcalNextVisitDate.delete(0,END)
                        mainwin.PcalNextVisitDate.insert(0,Prow[12])
                        mainwin.PtxtDescription.delete(0,END)
                        mainwin.PtxtDescription.insert(0,Prow[13])
                        mainwin.PtxtPrepayment.delete(0,END)
                        mainwin.PtxtPrepayment.insert(0,Prow[14])                        
                        mainwin.PtxtHospitalCost.delete(0,END)
                        mainwin.PtxtHospitalCost.insert(0,Prow[15])                         
                        mainwin.PtxtInsuranceShare.delete(0,END)
                        mainwin.PtxtInsuranceShare.insert(0,Prow[16])                         
                        mainwin.PtxtRemainingCost.delete(0,END)
                        mainwin.PtxtRemainingCost.insert(0,Prow[17])                            
                        Psexuality.set(value=Prow[6])
                        
                        
                        if Prow[6]=='Man' :
                            sx='Mr.'
                        else :
                            sx='Ms.'                      
        
                        PShowInf.delete(0,END)
                        PShowInf.insert(0,(sx ,Prow[1],Prow[2]))
                        PShowInf.insert(1,('NationalCode:',Prow[0]))
                        PShowInf.insert(2,('Tel:',Prow[5]))  
                        PShowInf.insert(3,('FileNumber:',Prow[7]))
                        PShowInf.insert(4,('TreatingDoctor:',Prow[8],'NationalCode:',PDNC))
                        PShowInf.insert(5,('HospitalizationDate:',Prow[10]))
                        PShowInf.insert(6,('DischargeDate:',Prow[11])) 
                        PShowInf.insert(7,('NextVisitDay:',Prow[12]))  
                        PShowInf.insert(8,('Description:',Prow[13]))
                        PShowInf.insert(9,('Prepayment=',Prow[14]))
                        PShowInf.insert(10,('HospitalCost=',Prow[15],'InsuranceShare=',Prow[16]))  
                        PShowInf.insert(11,('RemainingCost=',Prow[17]))                     
                        PShowInf.insert(12,('Address:',Prow[4],'PostalCode:',Prow[3]))               
                        
                        D_CSV_FILE = 'Doctors.csv'
                        with open(D_CSV_FILE, 'r') as fD:
                                        Dreader = csv.reader(fD)
                                        for Drow in Dreader:
                                            if Drow!=[] and PDNC == Drow[0]:
                                                
                                                mainwin.DtxtNC.delete(0,END)
                                                mainwin.DtxtNC.insert(0,Drow[0])
                                                mainwin.DtxtFn.delete(0,END)
                                                mainwin.DtxtFn.insert(0,Drow[1])                                                
                                                mainwin.DtxtLn.delete(0,END)
                                                mainwin.DtxtLn.insert(0,Drow[2])
                                                mainwin.DtxtCP.delete(0,END)
                                                mainwin.DtxtCP.insert(0,Drow[3])
                                                mainwin.DtxtAdr.delete(0,END)
                                                mainwin.DtxtAdr.insert(0,Drow[4])
                                                mainwin.DtxtTel.delete(0,END)
                                                mainwin.DtxtTel.insert(0,Drow[5])
                                                Dsexuality.set(value=Drow[6]) 
                                                mainwin.DtxtPreviousRemainder.delete(0,END)
                                                mainwin.DtxtPreviousRemainder.insert(0,Drow[7])                      
                                                mainwin.DtxtSalary.delete(0,END)
                                                mainwin.DtxtSalary.insert(0,Drow[8]) 
                                                mainwin.DtxtRemainderSalary.delete(0,END)
                                                mainwin.DtxtRemainderSalary.insert(0,Drow[9])
                                                
                                                if Drow[6]=='Man' :
                                                    Dsx='Mr.'
                                                else :
                                                    Dsx='Ms.'                                                 
                                                
                                                DShowInf.delete(0,END)
                                                DShowInf.insert(0,(Dsx ,Drow[1],Drow[2]))
                                                DShowInf.insert(1,('NationalCode:',Drow[0]))
                                                DShowInf.insert(2,('Tel:',Drow[5]))  
                                                DShowInf.insert(9,('PreviousRemainder=',Drow[7]))
                                                DShowInf.insert(10,('Salary=',Drow[8]))  
                                                DShowInf.insert(11,('RemainderSalary=',Drow[9]))                     
                                                DShowInf.insert(12,('Address:',Drow[4],'PostalCode:',Drow[3]))                                                
                                              
                                                
                                                
                if pat==False :
                    messagebox.showerror("The national code of the patient is not correct or is not exist", "Please correct The national code or add the patient to the patient database")                                                  

            


        def DShow_inf():
            
            DNC=mainwin.DtxtNC.get()


            D_CSV_FILE = 'Doctors.csv'

            with open(D_CSV_FILE, 'r') as fD:
                Dreader = csv.reader(fD)
                Doct=False

                for Drow in Dreader:
                    if Drow!=[] and DNC == Drow[0]:
                        
                        Doct=True
                        mainwin.DtxtFn.delete(0,END)
                        mainwin.DtxtFn.insert(0,Drow[1])
                        mainwin.DtxtLn.delete(0,END)
                        mainwin.DtxtLn.insert(0,Drow[2])
                        mainwin.DtxtCP.delete(0,END)
                        mainwin.DtxtCP.insert(0,Drow[3])
                        mainwin.DtxtAdr.delete(0,END)
                        mainwin.DtxtAdr.insert(0,Drow[4])
                        mainwin.DtxtTel.delete(0,END)
                        mainwin.DtxtTel.insert(0,Drow[5])
                        Dsexuality.set(value=Drow[6])
                        mainwin.DtxtPreviousRemainder.delete(0,END)
                        mainwin.DtxtPreviousRemainder.insert(0,Drow[7])                        
                        mainwin.DtxtSalary.delete(0,END)
                        mainwin.DtxtSalary.insert(0,Drow[8])                         
                        mainwin.DtxtRemainderSalary.delete(0,END)
                        mainwin.DtxtRemainderSalary.insert(0,Drow[9]) 

                        if Drow[6]=='Man' :
                            Dsx='Mr.'
                        else :
                            Dsx='Ms.'                      
            
                        DShowInf.delete(0,END)
                        DShowInf.insert(0,(Dsx ,Drow[1],Drow[2]))
                        DShowInf.insert(1,('NationalCode:',Drow[0]))
                        DShowInf.insert(2,('Tel:',Drow[5]))  
                        DShowInf.insert(9,('PreviousRemainder=',Drow[7]))
                        DShowInf.insert(10,('Salary=',Drow[8]))  
                        DShowInf.insert(11,('RemainderSalary=',Drow[9]))                     
                        DShowInf.insert(12,('Address:',Drow[4],'PostalCode:',Drow[3]))
                        
                        
            #     if Doct==False :
            #         messagebox.showerror("The national code of the doctor is not correct or is not exist", "Please correct The national code or add the doctor to the doctors database")                                              
            # fD.close()

            
        def PClear():
            PShowInf.delete(0,END)
            mainwin.PtxtNC.delete(0,END)
            mainwin.PtxtFn.delete(0,END)
            mainwin.PtxtLn.delete(0,END)
            mainwin.PtxtCP.delete(0,END)
            mainwin.PtxtAdr.delete(0,END)
            mainwin.PtxtTel.delete(0,END)
            Psexuality.set(0) 
            mainwin.PtxtRFN.delete(0,END)
            mainwin.Pdoctor.delete(0,END)
            mainwin.PdoctorNC.delete(0,END)
            mainwin.PcalHospitalizationDate.delete(0,END)
            mainwin.PcalDischargeDate.delete(0,END)
            mainwin.PcalNextVisitDate.delete(0,END)
            mainwin.PtxtDescription.delete(0,END)
            mainwin.PtxtPrepayment.delete(0,END)
            mainwin.PtxtHospitalCost.delete(0,END)
            mainwin.PtxtInsuranceShare.delete(0,END)
            mainwin.PtxtRemainingCost.delete(0,END)
            
            DShowInf.delete(0,END)
            mainwin.DtxtNC.delete(0,END)
            mainwin.DtxtFn.delete(0,END)
            mainwin.DtxtLn.delete(0,END)
            mainwin.DtxtCP.delete(0,END)
            mainwin.DtxtAdr.delete(0,END)
            mainwin.DtxtTel.delete(0,END)
            Dsexuality.set(0) 
            mainwin.DtxtPreviousRemainder.delete(0,END)
            mainwin.DtxtSalary.delete(0,END)
            mainwin.DtxtRemainderSalary.delete(0,END)
                          
          
            
                        
                        
        def DClear():
            DShowInf.delete(0,END)
            mainwin.DtxtNC.delete(0,END)
            mainwin.DtxtFn.delete(0,END)
            mainwin.DtxtLn.delete(0,END)
            mainwin.DtxtCP.delete(0,END)
            mainwin.DtxtAdr.delete(0,END)
            mainwin.DtxtTel.delete(0,END)
            Dsexuality.set(0) 
            mainwin.DtxtPreviousRemainder.delete(0,END)
            mainwin.DtxtSalary.delete(0,END)
            mainwin.DtxtRemainderSalary.delete(0,END)                        

            PShowInf.delete(0,END)
            mainwin.PtxtNC.delete(0,END)
            mainwin.PtxtFn.delete(0,END)
            mainwin.PtxtLn.delete(0,END)
            mainwin.PtxtCP.delete(0,END)
            mainwin.PtxtAdr.delete(0,END)
            mainwin.PtxtTel.delete(0,END)
            Psexuality.set(0) 
            mainwin.PtxtRFN.delete(0,END)
            mainwin.Pdoctor.delete(0,END)
            mainwin.PdoctorNC.delete(0,END)
            mainwin.PcalHospitalizationDate.delete(0,END)
            mainwin.PcalDischargeDate.delete(0,END)
            mainwin.PcalNextVisitDate.delete(0,END)
            mainwin.PtxtDescription.delete(0,END)
            mainwin.PtxtPrepayment.delete(0,END)
            mainwin.PtxtHospitalCost.delete(0,END)
            mainwin.PtxtInsuranceShare.delete(0,END)
            mainwin.PtxtRemainingCost.delete(0,END)  
            
            
        def PDelete():
            
            PNC=mainwin.PtxtNC.get()

            repeat=False
            with open("Patients.csv", 'r') as file, open("Patients1.csv", 'w') as fout:
                csvreader = csv.reader(file)
                csvwriter = csv.writer(fout)
                for row in csvreader:
                    if row!=[] and row[0]!= PNC :
                        csvwriter.writerow(row)
                    elif row!=[] and row[0]== PNC and repeat==True:
                        csvwriter.writerow(row)                        
                    elif row!=[] and row[0]== PNC and repeat==False:
                        repeat=True
                        
            file.close()
            fout.close()
            
            file = "Patients1.csv"
            location = "Patients.csv"
            path = os.replace(file, location) 
           
            PShowInf.delete(0,END)
            mainwin.PtxtNC.delete(0,END)
            mainwin.PtxtFn.delete(0,END)
            mainwin.PtxtLn.delete(0,END)
            mainwin.PtxtCP.delete(0,END)
            mainwin.PtxtAdr.delete(0,END)
            mainwin.PtxtTel.delete(0,END)
            Psexuality.set(0) 
            mainwin.PtxtRFN.delete(0,END)
            mainwin.Pdoctor.delete(0,END)
            mainwin.PdoctorNC.delete(0,END)
            mainwin.PcalHospitalizationDate.delete(0,END)
            mainwin.PcalDischargeDate.delete(0,END)
            mainwin.PcalNextVisitDate.delete(0,END)
            mainwin.PtxtDescription.delete(0,END)
            mainwin.PtxtPrepayment.delete(0,END)
            mainwin.PtxtHospitalCost.delete(0,END)
            mainwin.PtxtInsuranceShare.delete(0,END)
            mainwin.PtxtRemainingCost.delete(0,END)
            
            DShowInf.delete(0,END)
            mainwin.DtxtNC.delete(0,END)
            mainwin.DtxtFn.delete(0,END)
            mainwin.DtxtLn.delete(0,END)
            mainwin.DtxtCP.delete(0,END)
            mainwin.DtxtAdr.delete(0,END)
            mainwin.DtxtTel.delete(0,END)
            Dsexuality.set(0) 
            mainwin.DtxtPreviousRemainder.delete(0,END)
            mainwin.DtxtSalary.delete(0,END)
            mainwin.DtxtRemainderSalary.delete(0,END)  
            
            
        def DDelete():
            
            DNC=mainwin.DtxtNC.get()

            repeat=False
            with open("Doctors.csv", 'r') as file, open("Doctors1.csv", 'w') as fout:
                csvreader = csv.reader(file)
                csvwriter = csv.writer(fout)
                for Drow in csvreader:
                    if Drow!=[] and Drow[0]!= DNC :
                        csvwriter.writerow(Drow) 
                    elif Drow!=[] and Drow[0]== DNC and repeat==True:
                        csvwriter.writerow(Drow)                        
                    elif Drow!=[] and Drow[0]== DNC and repeat==False:
                        repeat=True
                                                    

            file.close()
            fout.close()
            
            file = "Doctors1.csv"
            location = "Doctors.csv"
            path = os.replace(file, location) 


                              
            DShowInf.delete(0,END)
            mainwin.DtxtNC.delete(0,END)
            mainwin.DtxtFn.delete(0,END)
            mainwin.DtxtLn.delete(0,END)
            mainwin.DtxtCP.delete(0,END)
            mainwin.DtxtAdr.delete(0,END)
            mainwin.DtxtTel.delete(0,END)
            Dsexuality.set(0) 
            mainwin.DtxtPreviousRemainder.delete(0,END)
            mainwin.DtxtSalary.delete(0,END)
            mainwin.DtxtRemainderSalary.delete(0,END)                        

            PShowInf.delete(0,END)
            mainwin.PtxtNC.delete(0,END)
            mainwin.PtxtFn.delete(0,END)
            mainwin.PtxtLn.delete(0,END)
            mainwin.PtxtCP.delete(0,END)
            mainwin.PtxtAdr.delete(0,END)
            mainwin.PtxtTel.delete(0,END)
            Psexuality.set(0) 
            mainwin.PtxtRFN.delete(0,END)
            mainwin.Pdoctor.delete(0,END)
            mainwin.PdoctorNC.delete(0,END)
            mainwin.PcalHospitalizationDate.delete(0,END)
            mainwin.PcalDischargeDate.delete(0,END)
            mainwin.PcalNextVisitDate.delete(0,END)
            mainwin.PtxtDescription.delete(0,END)
            mainwin.PtxtPrepayment.delete(0,END)
            mainwin.PtxtHospitalCost.delete(0,END)
            mainwin.PtxtInsuranceShare.delete(0,END)
            mainwin.PtxtRemainingCost.delete(0,END)  

        def Pupdate():

            PPrepayment=int(mainwin.PtxtPrepayment.get())
            HospitalCost=int(mainwin.PtxtHospitalCost.get())
            InsuranceShare=int(mainwin.PtxtInsuranceShare.get())
            RemainingCost=HospitalCost-PPrepayment-InsuranceShare
            
            mainwin.PtxtRemainingCost.delete(0,END)
            mainwin.PtxtRemainingCost.insert(0,RemainingCost)
            sex=Psexuality.get()
            d1=mainwin.PcalHospitalizationDate.get()
            d2=mainwin.PcalDischargeDate.get()
            d3=mainwin.PcalNextVisitDate.get()
              
            if sex=='Man' :
                sx='Mr.'
            else :
                sx='Ms.'
                
            PD=mainwin.Pdoctor.get()
            PDNC=mainwin.PdoctorNC.get()

            # Open the CSV file for writing
            with open("Patients.csv", mode="a", newline="\n") as Pcsv_file:

                csv_writer = csv.writer(Pcsv_file)
                csv_writer.writerow([])
                csv_writer.writerow([mainwin.PtxtNC.get(),mainwin.PtxtFn.get(),mainwin.PtxtLn.get(),mainwin.PtxtCP.get(),mainwin.PtxtAdr.get(),mainwin.PtxtTel.get(),sex,mainwin.PtxtRFN.get(),PD,PDNC,d1,d2,d3,mainwin.PtxtDescription.get(),PPrepayment,HospitalCost,InsuranceShare,RemainingCost])

            Pcsv_file.close()
            
            PShowInf.delete(0,END)
            PShowInf.insert(0,(sx ,mainwin.PtxtFn.get(),mainwin.PtxtLn.get()))
            PShowInf.insert(1,('NationalCode:',mainwin.PtxtNC.get()))
            PShowInf.insert(2,('Tel:',mainwin.PtxtTel.get()))  
            PShowInf.insert(3,('FileNumber:',mainwin.PtxtRFN.get()))
            PShowInf.insert(4,('TreatingDoctor:',PD,'NationalCode:',PDNC))
            PShowInf.insert(5,('HospitalizationDate:',d1))
            PShowInf.insert(6,('DischargeDate:',d2)) 
            PShowInf.insert(7,('NextVisitDay:',d3))  
            PShowInf.insert(8,('Description:',mainwin.PtxtDescription.get()))
            PShowInf.insert(9,('Prepayment=',PPrepayment))
            PShowInf.insert(10,('HospitalCost=',HospitalCost,'InsuranceShare=',InsuranceShare))  
            PShowInf.insert(11,('RemainingCost=',RemainingCost))                     
            PShowInf.insert(12,('Address:',mainwin.PtxtAdr.get(),'PostalCode:',mainwin.PtxtCP.get()))
        
            PDelete()
            
            
        def Dupdate():
            
            PreviousRemainder=int(mainwin.DtxtPreviousRemainder.get())
            Salary=int(mainwin.DtxtSalary.get())
            RemainderSalary=Salary+PreviousRemainder

            mainwin.DtxtRemainderSalary.delete(0,END)
            mainwin.DtxtRemainderSalary.insert(0,RemainderSalary)
            Dsex=Dsexuality.get()
              
            if Dsex=='Man' :
                Dsx='Mr.'
            else :
                Dsx='Ms.'

            
            # Open the CSV file for writing
            with open("Doctors.csv", mode="a", newline="\n") as csv_fileD:
                csv_writerD = csv.writer(csv_fileD)
                csv_writerD.writerow([])
                csv_writerD.writerow([mainwin.DtxtNC.get(),mainwin.DtxtFn.get(),mainwin.DtxtLn.get(),mainwin.DtxtCP.get(),mainwin.DtxtAdr.get(),mainwin.DtxtTel.get(),Dsex,PreviousRemainder,Salary,RemainderSalary])
            csv_fileD.close()

            DShowInf.delete(0,END)
            DShowInf.insert(0,(Dsx ,mainwin.DtxtFn.get(),mainwin.DtxtLn.get()))
            DShowInf.insert(1,('NationalCode:',mainwin.DtxtNC.get()))
            DShowInf.insert(2,('Tel:',mainwin.DtxtTel.get()))  
            DShowInf.insert(9,('PreviousRemainder=',PreviousRemainder))
            DShowInf.insert(10,('Salary=',Salary))  
            DShowInf.insert(11,('RemainderSalary=',RemainderSalary))                     
            DShowInf.insert(12,('Address:',mainwin.DtxtAdr.get(),'PostalCode:',mainwin.DtxtCP.get()))
      
            DDelete()
            
        def PackageExit():
            sys.exit()
            
            
            

              

        Exit_button = Button(root, text="Exit", font=("Arial", 14),width=15,command=PackageExit)
        Exit_button.place_forget() 
        
  
        PDataFrame=Frame(root,bd=1,width=600,height=750,padx=20,pady=20,relief=RIDGE ,bg="white smoke" )
        PDataFrame.place_forget()
        PButtonFrame=Frame(PDataFrame,bd=2,width=420,height=70,padx=18,pady=10,bg="white smoke" ,relief=RIDGE)
        PButtonFrame.pack(side=BOTTOM)        
        PDataFrameLEFT=LabelFrame(PDataFrame,bd=1,width=300,height=550,padx=20,relief=RIDGE,bg="white smoke" ,fg="red",font=('times new roman',22,'bold'),text="Patients Information\n")
        PDataFrameLEFT.pack(side=LEFT)
        PDataFrameRIGHT=LabelFrame(PDataFrame,bd=1,width=300,height=300,padx=30,pady=3,relief=RIDGE,bg="white smoke" ,font=('times new roman',22,'bold'),text="Details\n") 
        PDataFrameRIGHT.pack()
        PDataFrameRIGHT2=LabelFrame(PDataFrame,bd=1,width=300,height=275,padx=30,pady=3,relief=RIDGE,bg="white smoke" ,font=('times new roman',22,'bold'),text="Financial records\n") 
        PDataFrameRIGHT2.pack() 
 
        
        mainwin.PbtnAdd=Button(PButtonFrame,text='Add',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=Padd_data)
        mainwin.PbtnAdd.grid(row=0,column=0)

        mainwin.PbtnDisplay=Button(PButtonFrame,text='Show Inf.',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=PShow_inf )
        mainwin.PbtnDisplay.grid(row=0,column=1)

        mainwin.PbtnClear=Button(PButtonFrame,text='Clear',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=PClear)
        mainwin.PbtnClear.grid(row=0,column=2)  

        mainwin.PbtnDel=Button(PButtonFrame,text='Delete',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=PDelete)
        mainwin.PbtnDel.grid(row=0,column=3)

        mainwin.Pbtnupdate=Button(PButtonFrame,text='Update',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=Pupdate)
        mainwin.Pbtnupdate.grid(row=0,column=4)  
        
 
        DDataFrame=Frame(root,bd=1,width=600,height=750,padx=20,pady=20,relief=RIDGE ,bg="white smoke" )
        DDataFrame.place_forget()
        DButtonFrame=Frame(DDataFrame,bd=2,width=420,height=70,padx=18,pady=10,bg="white smoke" ,relief=RIDGE)
        DButtonFrame.pack(side=BOTTOM)         
        DDataFrameLEFT=LabelFrame(DDataFrame,bd=1,width=300,height=550,padx=20,relief=RIDGE,bg="white smoke" ,fg="red",font=('times new roman',22,'bold'),text="Doctors Information\n")
        DDataFrameLEFT.pack(side=LEFT)
        DDataFrameRIGHT=LabelFrame(DDataFrame,bd=1,width=300,height=300,padx=30,pady=3,relief=RIDGE,bg="white smoke" ,font=('times new roman',22,'bold'),text="Details\n") 
        DDataFrameRIGHT.pack()
        DDataFrameRIGHT2=LabelFrame(DDataFrame,bd=1,width=300,height=275,padx=30,pady=3,relief=RIDGE,bg="white smoke" ,font=('times new roman',22,'bold'),text="Financial records\n") 
        DDataFrameRIGHT2.pack() 

        
        mainwin.DbtnAdd=Button(DButtonFrame,text='Add',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=Dadd_data)
        mainwin.DbtnAdd.grid(row=0,column=0)

        mainwin.DbtnDisplay=Button(DButtonFrame,text='Show Inf.',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=DShow_inf )
        mainwin.DbtnDisplay.grid(row=0,column=1)

        mainwin.DbtnClear=Button(DButtonFrame,text='Clear',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=DClear)
        mainwin.DbtnClear.grid(row=0,column=2)  

        mainwin.DbtnDel=Button(DButtonFrame,text='Delete',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=DDelete)
        mainwin.DbtnDel.grid(row=0,column=3)

        mainwin.Dbtnupdate=Button(DButtonFrame,text='Update',font=('times new roman',16,'bold'),height=1,width=6,bd=4,command=Dupdate)
        mainwin.Dbtnupdate.grid(row=0,column=4) 
          
        
        mainwin.PlblFn=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Firstname',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblFn.grid(row=0,column=0,sticky=W)
        mainwin.PtxtFn=Entry(PDataFrameLEFT,font=('arial',14),textvariable=PFirstname,width=14)
        mainwin.PtxtFn.grid(row=0,column=1)

        mainwin.PlblLn=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Lastname',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblLn.grid(row=1,column=0,sticky=W)
        mainwin.PtxtLn=Entry(PDataFrameLEFT,font=('arial',14),textvariable=PLastname,width=14)
        mainwin.PtxtLn.grid(row=1,column=1) 
        
        mainwin.PlblNC=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='National Code',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblNC.grid(row=2,column=0,sticky=W)
        mainwin.PtxtNC=Entry(PDataFrameLEFT,font=('arial',14),textvariable=PNationalCode,width=14)
        mainwin.PtxtNC.grid(row=2,column=1)         
        
        mainwin.PlblCP=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Postal Code',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblCP.grid(row=3,column=0,sticky=W)
        mainwin.PtxtCP=Entry(PDataFrameLEFT,font=('arial',14),textvariable=PPostalCode,width=14)
        mainwin.PtxtCP.grid(row=3,column=1)  
        
        mainwin.PlblAdr=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Address',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblAdr.grid(row=4,column=0,sticky=W)
        mainwin.PtxtAdr=Entry(PDataFrameLEFT,font=('arial',10),textvariable=PAddress,width=22)
        mainwin.PtxtAdr.grid(row=4,column=1)                    
        
        mainwin.PlblTel=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Telphone',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblTel.grid(row=5,column=0,sticky=W)
        mainwin.PtxtTel=Entry(PDataFrameLEFT,font=('arial',14),textvariable=Ptelphone,width=14)
        mainwin.PtxtTel.grid(row=5,column=1) 
        
        mainwin.PlblSex=Label(PDataFrameLEFT,text='Sex',font=('times new roman',16,'bold'),bg="white smoke" ,fg='black')
        mainwin.PlblSex.grid(row=6,column=0,sticky=W)
        Psexuality=StringVar()
        
        mainwin.PSexType1=Radiobutton(PDataFrameLEFT,text='Man',font=('arial',14),variable=Psexuality,value='Man')
        mainwin.PSexType1.grid(row=6,column=1)  
        mainwin.PSexType2=Radiobutton(PDataFrameLEFT,text='Woman',font=('arial',14),variable=Psexuality,value='Woman')
        mainwin.PSexType2.grid(row=7,column=1) 
        
        mainwin.PlblRFN=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Rec.File No.',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblRFN.grid(row=8,column=0,sticky=W)
        mainwin.PtxtRFN=Entry(PDataFrameLEFT,font=('arial',14),textvariable=RecordFileNo,width=14)
        mainwin.PtxtRFN.grid(row=8,column=1) 
        
        mainwin.Pdoctor=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text="Treating Doctor",padx=2,pady=2,bg="white smoke" )
        mainwin.Pdoctor.grid(row=9,column=0,sticky=W)
        mainwin.Pdoctor=Entry(PDataFrameLEFT,font=('arial',14),textvariable=Pdoctor,width=14)
        mainwin.Pdoctor.grid(row=9,column=1)        

       
        mainwin.PdoctorNC=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text="Doc. National Code",padx=2,pady=2,bg="white smoke" )
        mainwin.PdoctorNC.grid(row=10,column=0,sticky=W)
        mainwin.PdoctorNC=Entry(PDataFrameLEFT,font=('arial',14),textvariable=PdoctorNC,width=14)
        mainwin.PdoctorNC.grid(row=10,column=1)         
     
        
        mainwin.PlblHospitalizationDate=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Hospitalization Date',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblHospitalizationDate.grid(row=11,column=0,sticky=W)
        mainwin.PcalHospitalizationDate=DateEntry(PDataFrameLEFT,selectmode='day',variable=HospitalizationDate)
        mainwin.PcalHospitalizationDate.grid(row=11,column=1,padx=15)     
                         
        mainwin.PlblDischargeDate=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Discharge Date',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblDischargeDate.grid(row=12,column=0,sticky=W)
        mainwin.PcalDischargeDate=DateEntry(PDataFrameLEFT,selectmode='day')
        mainwin.PcalDischargeDate.grid(row=12,column=1,padx=15)    
        
                     
        mainwin.PlblNextVisitDate=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Next Visit Date',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblNextVisitDate.grid(row=13,column=0,sticky=W)
        mainwin.PcalNextVisitDate=DateEntry(PDataFrameLEFT,selectmode='day')
        mainwin.PcalNextVisitDate.grid(row=13,column=1,padx=15) 
                

        mainwin.PlblDescription=Label(PDataFrameLEFT,font=('times new roman',14,'bold'),text='Description',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblDescription.grid(row=14,column=0,sticky=W)
        mainwin.PtxtDescription=Entry(PDataFrameLEFT,font=('arial',14),textvariable=Description,width=14)
        mainwin.PtxtDescription.grid(row=14,column=1) 
        
        mainwin.PlblPrepayment=Label(PDataFrameRIGHT2,font=('times new roman',14,'bold'),text='Prepayment',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblPrepayment.grid(row=0,column=0,sticky=W)
        PPrepayment=IntVar()
        mainwin.PtxtPrepayment=Entry(PDataFrameRIGHT2,font=('arial',14),textvariable=PPrepayment,width=14)
        mainwin.PtxtPrepayment.grid(row=0,column=1) 
        
        mainwin.PlblHospitalCost=Label(PDataFrameRIGHT2,font=('times new roman',14,'bold'),text='Hospital Cost',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblHospitalCost.grid(row=1,column=0,sticky=W)
        HospitalCost=IntVar()
        mainwin.PtxtHospitalCost=Entry(PDataFrameRIGHT2,font=('arial',14),textvariable=HospitalCost,width=14)
        mainwin.PtxtHospitalCost.grid(row=1,column=1)         
        
        mainwin.PlblInsuranceShare=Label(PDataFrameRIGHT2,font=('times new roman',14,'bold'),text='Insurance Share',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblInsuranceShare.grid(row=2,column=0,sticky=W)
        InsuranceShare=IntVar()
        mainwin.PtxtInsuranceShare=Entry(PDataFrameRIGHT2,font=('arial',14),textvariable=InsuranceShare,width=14)
        mainwin.PtxtInsuranceShare.grid(row=2,column=1)

        mainwin.PlblRemainingCost=Label(PDataFrameRIGHT2,font=('times new roman',14,'bold'),text='Remaining Cost',padx=2,pady=2,bg="white smoke" )
        mainwin.PlblRemainingCost.grid(row=3,column=0,sticky=W)
        RemainingCost=IntVar()
        mainwin.PtxtRemainingCost=Entry(PDataFrameRIGHT2,font=('arial',14),textvariable=RemainingCost,width=14)
        mainwin.PtxtRemainingCost.grid(row=3,column=1)    
            
        

        mainwin.DlblFn=Label(DDataFrameLEFT,font=('times new roman',14,'bold'),text='Firstname',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblFn.grid(row=0,column=0,sticky=W)
        mainwin.DtxtFn=Entry(DDataFrameLEFT,font=('arial',14),textvariable=DFirstname,width=14)
        mainwin.DtxtFn.grid(row=0,column=1)

        mainwin.DlblLn=Label(DDataFrameLEFT,font=('times new roman',14,'bold'),text='Lastname',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblLn.grid(row=1,column=0,sticky=W)
        mainwin.DtxtLn=Entry(DDataFrameLEFT,font=('arial',14),textvariable=DLastname,width=14)
        mainwin.DtxtLn.grid(row=1,column=1) 
        
        mainwin.DlblNC=Label(DDataFrameLEFT,font=('times new roman',14,'bold'),text='National Code',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblNC.grid(row=2,column=0,sticky=W)
        mainwin.DtxtNC=Entry(DDataFrameLEFT,font=('arial',14),textvariable=DNationalCode,width=14)
        mainwin.DtxtNC.grid(row=2,column=1)         
        
        mainwin.DlblCP=Label(DDataFrameLEFT,font=('times new roman',14,'bold'),text='Postal Code',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblCP.grid(row=3,column=0,sticky=W)
        mainwin.DtxtCP=Entry(DDataFrameLEFT,font=('arial',14),textvariable=DPostalCode,width=14)
        mainwin.DtxtCP.grid(row=3,column=1)  
        
        mainwin.DlblAdr=Label(DDataFrameLEFT,font=('times new roman',14,'bold'),text='Address',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblAdr.grid(row=4,column=0,sticky=W)
        mainwin.DtxtAdr=Entry(DDataFrameLEFT,font=('arial',10),textvariable=DAddress,width=22)
        mainwin.DtxtAdr.grid(row=4,column=1)                    
        
        mainwin.DlblTel=Label(DDataFrameLEFT,font=('times new roman',14,'bold'),text='Telphone',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblTel.grid(row=5,column=0,sticky=W)
        mainwin.DtxtTel=Entry(DDataFrameLEFT,font=('arial',14),textvariable=Dtelphone,width=14)
        mainwin.DtxtTel.grid(row=5,column=1) 
        
        mainwin.DlblSex=Label(DDataFrameLEFT,text='Sex',font=('times new roman',14,'bold'),bg="white smoke" ,fg='black')
        mainwin.DlblSex.grid(row=6,column=0,sticky=W)
        Dsexuality=StringVar()
        
        mainwin.DSexType1=Radiobutton(DDataFrameLEFT,text='Man',font=('arial',14),variable=Dsexuality,value='Man')
        mainwin.DSexType1.grid(row=6,column=1)  
        mainwin.DSexType2=Radiobutton(DDataFrameLEFT,text='Woman',font=('arial',14),variable=Dsexuality,value='Woman')
        mainwin.DSexType2.grid(row=7,column=1)   
        
        mainwin.DlblPreviousRemainder=Label(DDataFrameRIGHT2,font=('times new roman',14,'bold'),text='Pre. Remainder',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblPreviousRemainder.grid(row=1,column=0,sticky=W)
        PreviousRemainder=IntVar()
        mainwin.DtxtPreviousRemainder=Entry(DDataFrameRIGHT2,font=('arial',14),textvariable=PreviousRemainder,width=14)
        mainwin.DtxtPreviousRemainder.grid(row=1,column=1) 
        
        mainwin.DlblSalary=Label(DDataFrameRIGHT2,font=('times new roman',14,'bold'),text='Salary',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblSalary.grid(row=2,column=0,sticky=W)
        Salary=IntVar()
        mainwin.DtxtSalary=Entry(DDataFrameRIGHT2,font=('arial',14),textvariable=Salary,width=14)
        mainwin.DtxtSalary.grid(row=2,column=1)         
        
        mainwin.DlblRemainderSalary=Label(DDataFrameRIGHT2,font=('times new roman',14,'bold'),text='Remainder Salary',padx=2,pady=2,bg="white smoke" )
        mainwin.DlblRemainderSalary.grid(row=3,column=0,sticky=W)
        RemainderSalary=IntVar()
        mainwin.DtxtRemainderSalary=Entry(DDataFrameRIGHT2,font=('arial',14),textvariable=RemainderSalary,width=14)
        mainwin.DtxtRemainderSalary.grid(row=3,column=1)      

        

        Pscrollbar=Scrollbar(PDataFrameRIGHT)
        Pscrollbar.grid(row=0,column=1,sticky='ns')

        PShowInf=Listbox(PDataFrameRIGHT,width=25,height=12,font=('times new roman',12),yscrollcommand=Pscrollbar.set)
        PShowInf.bind('<<ListboxSelect>>',PDataFrameRIGHT)
        PShowInf.grid(row=0,column=0,padx=8)
        Pscrollbar.config(command=PShowInf.yview)

        Dscrollbar=Scrollbar(DDataFrameRIGHT)
        Dscrollbar.grid(row=0,column=1,sticky='ns')

        DShowInf=Listbox(DDataFrameRIGHT,width=25,height=12,font=('times new roman',12),yscrollcommand=Dscrollbar.set)
        DShowInf.bind('<<ListboxSelect>>',DDataFrameRIGHT)
        DShowInf.grid(row=0,column=0,padx=8)
        Dscrollbar.config(command=DShowInf.yview)
        
        

      
        
        
        def validate_login():
                    
                    userid = username_entry.get()
                    password = password_entry.get()
                    userpassok=False
                    
                    UserPass_FILE = 'UserPass.csv'
                    with open(UserPass_FILE, 'r') as fu:
                        reader = csv.reader(fu)
                        for urow in reader:
                            if userid == urow[0] and password == urow[1]:
                                Toplevel.destroy(rootlogin)
                                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                                button_open.place_forget()
                                ContactUs.place_forget()
                                label.pack_forget()
                                
                                Exit_button.place(x=1200,y=10)
                                
                                PDataFrame.place(x=10,y=50)
                                DDataFrame.place(x=800,y=50)
                                userpassok=True
                    
                    if userpassok==False :
                        messagebox.showerror("Login Failed", "Invalid username or password")
                    


        # Create and place the username label and entry
        username_label = Label(rootlogin, text="Username:",font=(14))
        username_label.pack()

        username_entry = Entry(rootlogin)
        username_entry.pack()

        # Create and place the password label and entry
        password_label = Label(rootlogin, text="Password:",font=("Arial", 14))
        password_label.pack()

        password_entry = Entry(rootlogin, show="*")  # Show asterisks for password
        password_entry.pack()
        

      

        # Create and place the login button
        login_button = Button(rootlogin, text="Login", command=validate_login,font=("Arial", 14))
        login_button.pack()
        
        
def open_login_window():
    rootlogin=Toplevel()
    application2=loginwindow(root,rootlogin)

def ContactUs_window():
    secondary_window = Toplevel()
    secondary_window.title("Sina Hospital Administration")
    secondary_window.config(width=550, height=150)
    Label(secondary_window,text="Dear user,\n Please email the hospital manager if you have any problems:\n administrator@sina.com  ",fg='red',font=("Arial", 14)).place(x=10, y=20)
    # Create a button to close (destroy) this window.
    button_close = Button(secondary_window,text="Close window",command=secondary_window.destroy)
    button_close.place(x=225, y=100)


class ImageLabel(Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)




   
          
       
if __name__=="__main__":
    root=Tk()
    
    application1=mainwindow(root)
    photo = PhotoImage(file = "1.gif")
    label = ImageLabel(root, text='Sina Hospital',font=("Arial", 60,"bold"), compound='center')
    label.pack()
    label.load('1.gif')
    
    button_open = Button(root,text="User Login",font=("Arial", 24,"bold"),command=open_login_window)
    button_open.place(x=650, y=500)
    
    ContactUs = Button(root,text="Contact Admin.",font=("Arial", 24,"bold"),command=ContactUs_window)
    ContactUs.place(x=620, y=650) 
     
      
    root.mainloop()     