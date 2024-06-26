import subprocess
import os
import webbrowser

directory_path = r'C:\abacus-src\deploy\ab-docker'
UpOrDown = ''
environment_Choice = ''

#Frontend Paths
AssetFrontendPath = r'C:\abacus-src\modules\Infinite.Microservices\Asset\src\Infinite.Asset.Web'
ConfigFrontendPath = r'C:\abacus-src\modules\Infinite.Microservices\AbacusConfig\src\Infinite.AbacusConfig.Portal'
AdminFrontendPath = r'C:\abacus-src\modules\Infinite.Microservices\AbacusAdmin\src\Infinite.AbacusAdmin.Portal'
FlowFrontendPath = r'C:\abacus-src\modules\Infinite.Microservices\AbacusFlow\src\Infinite.AbacusFlow.Portal'
BusinessPartnerFrontendPath = r'C:\abacus-src\modules\Infinite.Microservices\BusinessPartner\src\Infinite.BusinessPartner.Web'
SystemInformationFrontendPath = r'C:\abacus-src\modules\Infinite.Microservices\AbacusSystemInformation\src\Infinite.AbacusSystemInformation.Portal'

#Backend Paths
AssetBackendPath = r"C:\abacus-src\modules\Infinite.Microservices\Asset\src\Infinite.Asset.sln"
ConfigBackendPath = r"C:\abacus-src\modules\Infinite.Microservices\Abacus\src\Abacus.sln"
AdminBackendPath = r"C:\abacus-src\modules\Infinite.Microservices\AbacusAdmin\src\Infinite.AbacusAdmin.sln"
FlowBackendPath = r"C:\abacus-src\modules\Infinite.Microservices\AbacusFlow\src\Infinite.AbacusFlow.sln"
BusinessPartnerBackendPath = r"C:\abacus-src\modules\Infinite.Microservices\BusinessPartner\src\Infinite.BusinessPartner.sln"
SystemInformationBackendPath = r"C:\abacus-src\modules\Infinite.Microservices\AbacusSystemInformation\src\Infinite.AbacusSystemInformation.sln"

#Flags
ShouldOpenAdmin = False
ShouldOpenConfig = False
ShouldOpenAsset = False
ShouldOpenFlow = False
ShouldOpenBusinessPartner = False
ShouldOpenSystemInformation = False

def UpDownEnvironment(directory, command):
    # Change the current working directory
    os.chdir(directory)
    
    # Execute the command
    # Execute the command in a new terminal window
    result = subprocess.Popen(['cmd', '/k', command], creationflags=subprocess.CREATE_NEW_CONSOLE)

    if result is not None:
        print(f"Environment Is {UpOrDown}-ing...")
    else:
        print("Command execution failed, Please ensure you have the relevant configurations set up")

def OpenBackAndFrontend(directory, command, BackendPath):
    # Change the current working directory
    os.chdir(directory)
    
    # Execute the command
    # Execute the command in a new terminal window
    os.startfile(BackendPath)
    result = subprocess.run(command, shell=True, check=True)
    if result is not None:
        print(f"Installing Nuget Packages...")
        install = subprocess.run("npm i", shell=True, check=True)
    else:
        print("Command execution failed, Please ensure you have the relevant configurations set up")

def OpenSolutions():
    if ShouldOpenAdmin:
        OpenBackAndFrontend(AdminFrontendPath, 'code .', AdminBackendPath)
    if ShouldOpenAsset:
        OpenBackAndFrontend(AssetFrontendPath, 'code .', AssetBackendPath)
    if ShouldOpenConfig:
        OpenBackAndFrontend(ConfigFrontendPath, 'code .', ConfigBackendPath)
    if ShouldOpenFlow:
        OpenBackAndFrontend(FlowFrontendPath, 'code .', FlowBackendPath)
    if ShouldOpenBusinessPartner:
        OpenBackAndFrontend(BusinessPartnerFrontendPath, 'code .', BusinessPartnerBackendPath)
    if ShouldOpenSystemInformation:
        OpenBackAndFrontend(SystemInformationFrontendPath, 'code .', SystemInformationBackendPath)

 
def EnvironmentUpDown():
    print('Do you wish to up or down an environment?')
    print('Up Environment = 1')
    print('Down Environment = 2')

def MarketChoice():
    print('Which Market Do You Wish to Up. Choices: ')
    print('NL = 1')
    print('JP = 2')
    print('KR = 3')

def OpenLocalhost():
    if ChoiceInput == '1':
        url = 'http://localhost:4444'
    elif ChoiceInput == '2':
        url = 'http://localhost:8888'
    elif ChoiceInput == '3':
        url = 'http://localhost:9999'
    webbrowser.open(url)


# Updated directory path
EnvironmentUpDown()
command_choice = input("Please make a choice: ")

if command_choice == '1':
    UpOrDown = 'up'
elif command_choice == '2':
    UpOrDown = 'down'

MarketChoice()
ChoiceInput = input("Enter the market choice: ")
if ChoiceInput == '1':
    environment_Choice = 'nl'
elif ChoiceInput == '2':
    environment_Choice = 'jp'
elif ChoiceInput == '3':
    environment_Choice = 'kr'


command_to_execute = rf'.\{UpOrDown} {environment_Choice}'

UpDownEnvironment(directory_path, command_to_execute)
if UpOrDown == 'up':
    AdminOpen = input("Do You Wish To Open Admin y/n?")
    if AdminOpen == 'y':
        ShouldOpenAdmin = True

    AssetOpen = input("Do You Wish To Open Asset y/n?")
    if AssetOpen == 'y':
        ShouldOpenAsset = True

    ConfigOpen = input("Do You Wish To Open Config y/n?")
    if ConfigOpen == 'y':
        ShouldOpenConfig = True

    FlowOpen = input("Do You Wish To Open Flow y/n?")
    if FlowOpen == 'y':
        ShouldOpenFlow = True

    BusinessPartnerOpen = input("Do You Wish To Open BusinessPartner y/n?")
    if BusinessPartnerOpen == 'y':
        ShouldOpenBusinessPartner = True

    SystemInformationOpen = input("Do You Wish To Open System Information y/n?")
    if SystemInformationOpen == 'y':
        ShouldOpenSystemInformation = True

    OpenLocalhost()
    OpenSolutions()