# Import the required libraries
import os

#________________________________________________________________________________________________________________

# NB: Every function begin with the os.system("clear") instruction,
#     to clear the console between each action for clarity sake

# allow to display the contact as Nom: name, Prénom: surname, Email: mailAdress

def contactInfoParserPrinter(contact:str):
    contactInfos = contact.split(" | ")
    print("Nom:", contactInfos[0],", Prénom:", contactInfos[1],", Email:", contactInfos[2])

#________________________________________________________________________________________________________________
# Add contact to the file
def addContact(contactsList: list, pathContactsFile: str):

    os.system("clear")
    
    # Prompt the user successively for the name, the surname and
    # the email of the contact, the three variables are stored
    # separated and concatenanted after in case of evolution of the application
    print("~~~~~~~ Ajout d'un nouveau contact ~~~~~~~ \n \n")
    name = str(input("\
Veuillez entrer successivement le nom, le prénom et \n\
l'adresse mail de la personne à ajouter dans vos contacts:\n-> Nom: "))
    surname = str(input("-> Prénom: "))
    mail = str(input("-> Email: "))
    
    # Concatenation of the three variable using a pipe as a separator
    contactInfo = " | ".join([name, surname, mail])

    # Add the contact to the list 
    contactsList.append(contactInfo)

    # Add the contact at the end of the file
    with open(pathContactsFile, "a") as contactsFile:
        try:
            contactsFile.write(contactInfo)
            contactInfoParserPrinter(contactInfo)
        except Exception as e:
            print("Erreur lors de l'enregistrement du fichier de contacts")

#________________________________________________________________________________________________________________
# Reading contacts from the file, if the "alphabetical" parameter
def readContacts(contactsList: list, pathContactsFile: str, alphabetical: bool):

        os.system("clear")

        # Nice header to indicate that we display the contact list
        print("~~~~~~~~~~~~~~~~~~~~~ Mes contacts ~~~~~~~~~~~~~~~~~~~~~ \n \n")

        # If the user want to do so, sort alphabetically the contact list, the contact
        # list field is then rewritten in the alphabetical order too
        if alphabetical == True:
            
            contactsList = sorted(contactsList, key=str.lower)

            # Rewrite the contact.txt file with the alphabetically sorted
            # list
            with open(pathContactsFile, "w") as contactsFile:

                contactsFileTxt = "\n".join(contactsList)
                try:
                    contactsFile.write(contactsFileTxt)
                except Exception as e:
                    print("Erreur lors de l'enregistrement du fichier de contacts")

        # Iteration throught contactsList to print each contact
        for i in range(0, len(contactsList), 1):
              contactInfoParserPrinter(contactsList[i])

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#________________________________________________________________________________________________________________
# Count the contacts
def countContacts(contactsList: str):

    os.system("clear")

    # The number of contacts is simply the lenght of the contactList list
    print("-> Votre répertoire contient", len(contactsList), "contacts.")

#________________________________________________________________________________________________________________
# Search a contact
def searchContact(contactsList: str, searchedTerm: str):
    
    os.system("clear")

    foundContacts = []

    # For each contact in the contact list check if the searchedTerm is equal to name
    for contact in contactsList:

        # The contact string name | surname | emailAdress is spliter into a
        # list as [name, surname, emailAdress]
        contactInfos = contact.split(" | ")

        # if searchedTerm is contained in the name of the contact
        if searchedTerm.lower() in contactInfos[0].lower():

            foundContacts.append(contact)

    # If there is more than one person found
    if len(foundContacts) > 1:

        selectedContact = len(foundContacts) + 10

        while selectedContact >= len(foundContacts) or selectedContact < 0:

            print("Vous avez plusieurs contacts possibles, entrez l'index\n"\
                "du contact souhaité")
            
            for i in range(0, len(foundContacts), 1):
                print(i+1,"- ")
                contactInfoParserPrinter(foundContacts[i])
        
            selectedContact = int(input("-> "))-1

            if selectedContact >= len(foundContacts) or selectedContact < 0:
                print("Vous avez entré un index ne figurant pas dans la liste !\n")

        return foundContacts[selectedContact]
    
    elif len(foundContacts) == 1:

        return foundContacts[0]
    
    else:

        return "Aucun contact trouvé"

#________________________________________________________________________________________________________________
# Modification of a contact
def modifyContact(contactsList: str, searchedTerm: str, pathContactsFile: str):

    os.system("clear")

    # Search if the contact exist in the list
    foundContact = searchContact(contactsList, searchedTerm)

    # if the contact exist
    if foundContact != "Aucun contact trouvé":

        # Iteration through the contactsList, if the contact is found
        # the user is prompted to enter a new name, surname and mail
        # adress to update the entry in contactsList and the contact.txt
        # is rewritten
        for contact in range(0, len(contactsList), 1):

            if contactsList[contact].lower() == foundContact.lower():

                # The contact string name | surname | emailAdress is spliter into a
                # list as [name, surname, emailAdress]
                contactInfos = contactsList[contact].split(" | ")

                print("~~~~~~~ Modification d'un contact ~~~~~~~ \n \n")
                contactInfos[1] = str(input("\
Veuillez entrer successivement les nouveaux prénom et \n\
adresse mail de la personne:\n-> Prénom: "))
                contactInfos[2] = str(input("-> Email: "))
    
                # Concatenation of the three variable using a pipe as a separator
                contactInfo = " | ".join(contactInfos)

                contactsList[contact] = contactInfo
                
                with open(pathContactsFile, "w") as contactsFile:

                    contactsFileTxt = "\n".join(contactsList)

                    try:
                        contactsFile.write(contactsFileTxt)
                        print("Le contact de", contactInfos[0], contactInfos[1], "à été modifié !\n")

                    except Exception as e:
                        print("Erreur lors de l'enregistrement du fichier de contacts")

                return

    # If the contact doesn't exist return that it doesn't exist in the
    # contact list
    else:

        print(foundContact, "\n")

        return

#________________________________________________________________________________________________________________
# Deletion of a contact
def deleteContact(contactsList: str, searchedTerm: str, pathContactsFile: str):

    os.system("clear")

    # Search if the contact exist in the list
    foundContact = searchContact(contactsList, searchedTerm)
    
    # If the contact exist 
    if foundContact != "Aucun contact trouvé":

        # Iteration through the contactsList, if the contact is found
        # its entry in contactsList is removed and the contact.txt is
        # rewritten
        for contact in range(0, len(contactsList), 1):

            if contactsList[contact].lower() == foundContact.lower():

                contactsList.pop(contact)
                
                with open(pathContactsFile, "w") as contactsFile:

                    contactsFileTxt = "\n".join(contactsList)

                    try:
                        contactsFile.write(contactsFileTxt)
                        print("-> Le contact de", searchedTerm, "à été supprimé !\n")

                    except Exception as e:
                        print("Erreur lors de l'enregistrement du fichier de contacts")

                return

    # If the contact doesn't exist return that it doesn't exist in the
    # contact list
    else:
    
        print(foundContact, "\n")

        return