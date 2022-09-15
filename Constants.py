


#Club Constants
Organization = 'IEEE'
ActiveMembers = '62'
TCFUorIFCUBalance = '$0.00'
FSAAccountBalance = '$56.53'
OtherAccountBalance = '$0'
USGAward = '$2406.83'
DepartmentalAward = '$0'
ExternalSponsorship= '$0'
OtherIncome = '$0'
Location = "IEEE Lab Light Engineering 175" #assuming Event is held at Lab


#Questions' xpaths/necessary identifiers for each textbox/radio button on form

#Question 1
OrganizationDropDownxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]'
IEEEOptionxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[10]'

#Question 2
NumOfActiveMembersxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 3
TCFUTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 4
FSATextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 5
OtherAccountBalanceTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 6
USGAwardTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 7
DepartmentalAwardTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 8
ExternalSponsTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 9
OtherIncomeTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 10
EventNameTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 11
EventDescriptionTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea'

#Question 12
EventGoalTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 13
CollabsTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 14
StartDateTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'
EventStartTimeHTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input'
EventStartTimeMTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input'
EventStartTimeDropdownxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]'
AMStartOptionxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div[1]'
PMStartOptionxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div[2]'

#Question 15
EndDateTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'
EventEndTimeHTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input'
EventEndTimeMTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input'
EventEndTimeDropdownxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]'
AMEndOptionxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div[1]'
PMEndOptionxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div[2]'

#Question 16
LocationTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 17
ParticipationTextBoxxpath ='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea'

#Question 18
ExpenseRadioButtonxpath = '//*[@id="i42"]/div[3]/div' #only for Equipment and parts

#Question 19
ExplanationTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[2]/textarea'

#Question 20
UploadButtonxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[2]/span'

#Question 21
Vendors = {'Amazon': '//*[@id="i5"]/div[3]/div','Digikey':'//*[@id="i14"]/div[3]/div','Other':'//*[@id="i41"]'}
VendorOtherTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[13]/div/span/div/div/div[1]/input'

#Question 22
ItemNumberTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 23
ItemDescriptionTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'

#Question 24
QuantityPerPackageTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Questionn 25
CostPerPackageTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 26
NumberOfPackagesTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 27
ItemURLTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'

#Question 28
NeedByDateTextBoxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input'
NeedByTimeHTextboxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input'
NeedByTimeMTextboxxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div/div[1]/input'
NeedByTimeDropdownxpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]'
AMNeedOption = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div[1]'
PMNeedOption = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/div[2]'
