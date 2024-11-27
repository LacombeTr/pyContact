# Import the required libraries
import os
import utils

# Main function

# Check if the file "contacts.txt" exist, if not, the file is created
pathContactsFile = "contacts.txt"

doContactsFileExist = bool(os.path.exists(pathContactsFile))

if doContactsFileExist == False:

    with open(pathContactsFile, "w") as contactsFile:

        contactsFile.write("")
        print("\nFichier de contacts créé.\n")

# On crée une list en utilisant le fichier contact sur laquelle on travaillera
try:

    contactsFileTxt = open(pathContactsFile, "r").read()
    contactsList = contactsFileTxt.split("\n")

    print("Fichier de contact chargé avec succès\n")

except Exception as e:
    print("Erreur lors de la lecture du fichier: \n" + e)

# While the user does not send "stop" the app continue running
isAppRunning = bool(True)

while isAppRunning == True:

    # Giving the list of choices to the user (no indentation
    # in the print for displaying purposes)
    print("\
\n\
~~~~~~~~~~~~~~~~~~~~~~ PYCONTACT ~~~~~~~~~~~~~~~~~~~~~~~ \
\n\
Bienvenue dans votre nouveau gestionnaire de contacts \n\
PYCONTACT, quelle actions souhaitez vous executer ?\n\
\n\
1 - Ajouter un nouveau contact \n\
2 - Afficher les contacts \n\
3 - Trier et afficher les contacts dans l'ordre alphabétique \n\
4 - Compter les contacts \n\
5 - Rechercher un contact \n\
6 - Modifier un contact \n\
7 - Supprimer un contact \n\
stop - Quitter l'application \n\
\n\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
    
    # Prompting the user its choice based on the propositions above
    userAction = input("Que souhaitez vous faire ? \n-> ")
    print("\n")

    # For each case call the corresponding function
    match userAction:
        case "1":
        
            utils.addContact(contactsList, pathContactsFile)
        
        case "2":

            # Display to the user the contact list

            utils.readContacts(contactsList, pathContactsFile, alphabetical=False)
        
        case "3":

            # Sort the conact list in alphabetical order and display it to the
            # user.
            # Use readContacts but using the "alphabetical=true" parameter to
            # enable alphabetical sorting, prompting the user before this action
            # because this affect the .txt file 

            safetyWriting = input("\
You are about to sort and rewrite the contact file\n\
This action is definitive, are you sure about this ?\n\
Enter Y to proceed or any key to cancel this.\n-> ")       
            print("\n")

            if safetyWriting.lower() == "y":
                utils.readContacts(contactsList, pathContactsFile, alphabetical=True)
            else:
                print("Retour au menu principal")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        case "4":
        
            # Might be a bit too much to have function for this but for consistency
            # sake the logic is also put in a function

            utils.countContacts(contactsList)
        
        case "5":

            # Prompt the user for which contact they are looking for base either on the name,
            # the surname or the mail adress

            searchedTerm = str(input("Entrez le nom de la personne que vous recherchez:\n-> "))

            print("-> ")
            utils.contactInfoParserPrinter(utils.searchContact(contactsList, searchedTerm))
        
        case "6":
            
            # Prompting the user which entry he want to edit
            searchedTerm = str(input("\
Entrez le nom du contact que vous souhaiter modifier:\n\
(Attention cette action est irréversible)\n-> "))
            utils.modifyContact(contactsList, searchedTerm, pathContactsFile)
        
        case "7":

            # Prompting the user which entry he want to delete
            searchedTerm = str(input("\
Entrez le nom du contact que vous souhaiter effacer:\n\
(Attention cette action est irréversible)\n-> "))
            
            utils.deleteContact(contactsList, searchedTerm, pathContactsFile)
        
        case "stop":

            os.system("clear")

            # Changing isAppRunning to False to break the While loop
            isAppRunning = False

            # Asking confirmation to the user
            print("Vous aller quitter l'application, êtes-vous sûr ? \n-> ")
             
            userAction = input("Entrez Y si oui, entrez n'importe quel autre touche si non \n-> ")
            print("\n")

            if userAction.lower() != "y":

                # If the user change its mind changing back isAppRunning to True to stay
                # in the While loop
                isAppRunning = True
                print("Retour au menu principal")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            else:

                # Else indicate to the user that the application is shutting down
                print("Sortie de l'application \n \n")

        case _:

            os.system("clear")
            # If the option entered by the user is not one the proposed ones go back
            # to the main menu
            print("Je n'ai pas compris votre rêquête, retour au menu principal")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")