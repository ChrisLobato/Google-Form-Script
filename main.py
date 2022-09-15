from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
from Constants import*


options = Options()
options.add_argument("user-data-dir=C:\\Users\\Chris\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Profile 2")
driver = webdriver.Chrome(executable_path=r'C:\Users\Chris\Desktop\Google Form Script\chromedriver.exe', chrome_options=options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScr8smdzkpy2FzDxOZPF-GPiOP9Gd7ESj9ksOd0y3UGTwM9KQ/viewform")
time.sleep(2)

def clubInformation(driver):
    #Organization = 'IEEE'
    DropDownOrganization = driver.find_element("xpath",OrganizationDropDownxpath)
    DropDownOrganization.click()
    time.sleep(1)
    IEEEOPTION = driver.find_element("xpath",IEEEOptionxpath)
    IEEEOPTION.send_keys(Keys.SPACE)
    time.sleep(1)
    NumOfActiveMembers = driver.find_element("xpath",NumOfActiveMembersxpath)
    NumOfActiveMembers.send_keys(ActiveMembers)

    FirstNextButton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    FirstNextButton.click()
    time.sleep(2)

    TCFUTextBox = driver.find_element("xpath",TCFUTextBoxxpath)
    TCFUTextBox.send_keys(TCFUorIFCUBalance)

    FSATextBox = driver.find_element("xpath",FSATextBoxxpath)
    FSATextBox.send_keys(FSAAccountBalance)

    OtherAccountBalanceTextBox = driver.find_element("xpath",OtherAccountBalanceTextBoxxpath)
    OtherAccountBalanceTextBox.send_keys(OtherAccountBalance)

    USGAwardTextBox = driver.find_element("xpath",USGAwardTextBoxxpath)
    USGAwardTextBox.send_keys(USGAward)

    DepartmentalAwardTextBox = driver.find_element("xpath",DepartmentalAwardTextBoxxpath)
    DepartmentalAwardTextBox.send_keys(DepartmentalAward)

    ExternalSponsTextBox = driver.find_element("xpath",ExternalSponsTextBoxxpath)
    ExternalSponsTextBox.send_keys(ExternalSponsorship)

    OtherIncomeTextBox = driver.find_element("xpath",OtherIncomeTextBoxxpath)
    OtherIncomeTextBox.send_keys(OtherIncome)

def EventName(driver, name):
    EventName = name
    EventNameTextBox = driver.find_element("xpath",EventNameTextBoxxpath)
    EventNameTextBox.send_keys(EventName)

def EventDescription(driver, descrip):
    EventDescription = descrip
    EventDescriptionTextBox = driver.find_element("xpath",EventDescriptionTextBoxxpath)
    EventDescriptionTextBox.send_keys(EventDescription)

def EventGoal(driver, goal):
    EventGoal = goal
    EventGoalTextBox = driver.find_element("xpath",EventGoalTextBoxxpath)
    EventGoalTextBox.send_keys(EventGoal)

def Collabs(driver, org):
    Collabs = org
    CollabsTextBox = driver.find_element("xpath",CollabsTextBoxxpath)
    CollabsTextBox.send_keys(Collabs)

def EventStartDateNTime(driver, date, Atime):
    EventStartDate = date
    StartDateTextBox = driver.find_element("xpath",StartDateTextBoxxpath)
    StartDateTextBox.send_keys(EventStartDate)
    EventStartTime = Atime
    hours = EventStartTime[0:2]
    minutes = EventStartTime[3:5] 
    AMorPM= EventStartTime[-2:]
    EventStartTimeTextBox1 = driver.find_element("xpath",EventStartTimeHTextBoxxpath)
    EventStartTimeTextBox1.send_keys(hours)
    EventStartTimeTextBox2 = driver.find_element("xpath",EventStartTimeMTextBoxxpath)
    EventStartTimeTextBox2.send_keys(minutes)
    EventStartTimeAM_PM = driver.find_element("xpath",EventStartTimeDropdownxpath)
    EventStartTimeAM_PM.click()
    time.sleep(1)
    if (AMorPM == 'AM'):
        AMOption = driver.find_element("xpath",AMStartOptionxpath)
        AMOption.send_keys(Keys.SPACE)
    else:
        PMOption = driver.find_element("xpath",PMStartOptionxpath)
        PMOption.send_keys(Keys.SPACE)
    time.sleep(1)

def EventEndDateNTime(driver, date,Atime):
    EventEndDate = date
    EndDateTextBox = driver.find_element("xpath",EndDateTextBoxxpath)
    EndDateTextBox.send_keys(EventEndDate)
    EventEndTime = Atime
    hours = EventEndTime[0:2]
    minutes = EventEndTime[3:5] 
    AMorPM= EventEndTime[-2:]
    EventEndTimeTextBox1 = driver.find_element("xpath",EventEndTimeHTextBoxxpath)
    EventEndTimeTextBox1.send_keys(hours)
    EventEndTimeTextBox2 = driver.find_element("xpath",EventEndTimeMTextBoxxpath)
    EventEndTimeTextBox2.send_keys(minutes)
    EventEndTimeAMorPM = driver.find_element("xpath",EventEndTimeDropdownxpath)
    EventEndTimeAMorPM.click()
    time.sleep(1)
    if (AMorPM == 'AM'):
        AMOption = driver.find_element("xpath",AMEndOptionxpath)
        AMOption.send_keys(Keys.SPACE)
    else:
        PMOption = driver.find_element("xpath",PMEndOptionxpath)
        PMOption.send_keys(Keys.SPACE)
    time.sleep(1)

def EventLocation(driver):
    LocationTextBox = driver.find_element("xpath",LocationTextBoxxpath)
    LocationTextBox.send_keys(Location)

def ParticipationExpected(driver, numPeople):
    Participation = numPeople
    ParticipationTextBox = driver.find_element("xpath",ParticipationTextBoxxpath)
    ParticipationTextBox.send_keys(Participation)

def ExpenseType(driver):
    #for expense type we can do a dictionary of all the options and check if the
    #input/expense type matches with the option and we select it
    ExpenseRadioButtons = driver.find_element("xpath",ExpenseRadioButtonxpath)
    ExpenseRadioButtons.click()

def ExpenseExplanation(driver, explanation):
    ExpensesExplanation = explanation
    ExplanationTextBox = driver.find_element("xpath",ExplanationTextBoxxpath)
    ExplanationTextBox.send_keys(ExpensesExplanation)

def Vendor(driver, aVendor):
    chosenVendor = aVendor
    if(chosenVendor[:5]=="Other"):
        VendorButton = driver.find_element("xpath",Vendors[chosenVendor[:5]])
        VendorButton.click()
        VendorOtherTextBox = driver.find_element("xpath",VendorOtherTextBoxxpath)
        VendorOtherTextBox.send_keys(chosenVendor[7:])
    else:
        VendorButton = driver.find_element("xpath",Vendors[chosenVendor])
        VendorButton.click()

def ItemNum(driver, itemnum):
    ItemNumber = itemnum
    ItemNumberButton = driver.find_element("xpath",ItemNumberTextBoxxpath)
    ItemNumberButton.send_keys(ItemNumber)

def ItemDescription(driver, description):
    ItemDescription = description
    ItemDescriptionTextBox = driver.find_element("xpath",ItemDescriptionTextBoxxpath)
    ItemDescriptionTextBox.send_keys(ItemDescription)

def QuantperPackage(driver, quantity):
    QuantityPerPackage = quantity
    QuantityPerPackageTextBox = driver.find_element("xpath",QuantityPerPackageTextBoxxpath)
    QuantityPerPackageTextBox.send_keys(QuantityPerPackage)

def CostperPackage(driver, cost):
    CostPerPackage =cost
    CostPerPackageTextBox = driver.find_element("xpath",CostPerPackageTextBoxxpath)
    CostPerPackageTextBox.send_keys(CostPerPackage)

def NumPackages(driver, packages):
    NumberofPackages = packages
    NumberOfPackagesTextBox = driver.find_element("xpath",NumberOfPackagesTextBoxxpath)
    NumberOfPackagesTextBox.send_keys(NumberofPackages)

def ItemURL(driver, url):
    ItemPaymentURL = url
    ItemURLTextBox = driver.find_element("xpath",ItemURLTextBoxxpath)
    ItemURLTextBox.send_keys(ItemPaymentURL)

def NeedbyDateNTime(driver, date , Atime):
    NeedByDate = date
    NeedByDateTextBox = driver.find_element("xpath",NeedByDateTextBoxxpath)
    NeedByDateTextBox.send_keys(NeedByDate)
    NeedByTime = Atime
    Hours = NeedByTime[0:2]
    Minutes = NeedByTime[3:5]
    AMorPM = NeedByTime[-2:]
    NeedHoursTextBox = driver.find_element("xpath",NeedByTimeHTextboxxpath)
    NeedHoursTextBox.send_keys(Hours)
    NeedMinutesTextBox = driver.find_element("xpath",NeedByTimeMTextboxxpath)
    NeedMinutesTextBox.send_keys(Minutes)

    NeedTimeAMorPM = driver.find_element("xpath",NeedByTimeDropdownxpath)
    NeedTimeAMorPM.click()
    time.sleep(1)
    if (AMorPM == 'AM'):
        AMOption = driver.find_element("xpath",AMNeedOption)
        AMOption.send_keys(Keys.SPACE)
    else:
        PMOption = driver.find_element("xpath",PMNeedOption)
        PMOption.send_keys(Keys.SPACE)
    time.sleep(1)
#Actual script
with open("Soldering_Wiring_Curiosity workshop CSV - Sheet1 (2).csv", 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
        clubInformation(driver)
        SecondNextButton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
        SecondNextButton.click()
        time.sleep(2)
        EventName(driver, row[0])
        EventDescription(driver, row[1])
        EventGoal(driver, row[2])
        Collabs(driver, row[3])
        EventStartDateNTime(driver, row[4],row[5])
        EventEndDateNTime(driver, row[6],row[7])
        EventLocation(driver)
        ParticipationExpected(driver, row[8])
        ExpenseType(driver)
        ExpenseExplanation(driver, row[10])

        UploadButton = driver.find_element("xpath",UploadButtonxpath)
        UploadButton.click()
        UserInput = "No"
        print("Submitting form for: "+ row[0])
        print("Item: " + row[12])
        while (UserInput == "No"):
            UserInput = input("Finished Uploading?")

        ThirdNextButton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
        ThirdNextButton.click()
        time.sleep(2)
        Vendor(driver, row[11])
        ItemNum(driver, row[12])
        ItemDescription(driver, row[13])
        QuantperPackage(driver, row[14])
        CostperPackage(driver, row[15])
        NumPackages(driver, row[16])
        ItemURL(driver, row[17])
        NeedbyDateNTime(driver, row[18], row[19])
        SubmittedForm = "No"
        while(SubmittedForm=="No"):
            SubmittedForm= input("Submited Form?")
        # clearFormButton = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[2]/div[2]/div/span/span')
        # clearFormButton.click()
        # time.sleep(1)
        # ConfirmClear = driver.find_element("xpath",'/html/body/div[3]/div/div[2]/div[3]/div[2]')
        # ConfirmClear.click()
        time.sleep(2)
driver.quit()