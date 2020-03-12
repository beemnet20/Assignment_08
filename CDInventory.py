#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# BWorkeneh, 2020-Mar-09, modified code 
#------------------------------------------#
import pickle
# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        None

    """
    def __init__(self, cdId, cdTitle, cdArtist):
    #   -- Attributes  -- #
        self.__cd_id = cdId
        self.__cd_title = cdTitle
        self.__cd_artist = cdArtist
        
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter 
    def cd_id(self, value):
        if type(value) is int:
            self.__cd_id = int(value)
        else:
            raise Exception('The ID has to be an integer')
            
    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self, value):
        if str(value) == '':
            raise Exception('The title cannot be empty')
        else:
            self.__title = str(value)
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self, value):
        if str(value) == '':
            raise Exception('The artist cannot be empty')
        else:
            self.__cd_artist= str(value)
               
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_CDObjects): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name, lst_CDObjects):
        """ save inventory to a binary file
        Args:
            file_name (str): file to open to save CD inventory to
            lst_CDObjects(list of obj): list of CD objects to write into file
        Return: None
        """
        with open(file_name, 'wb') as objFile:
            pickle.dump(lst_CDObjects, objFile)

    @staticmethod
    def load_inventory(file_name, lst_CDObjects):
        """ load inventory from a binary file
        Args:
            file_name(str): file to open to load CD data from
        Return:
            a list of CD objects
        """
        try:
            with open(file_name, 'rb') as objFile:
                lst_CDObjects = pickle.load(objFile)
                return lst_CDObjects 
        except FileNotFoundError:
            print("The file {} could not be loaded".format(file_name))
            return lst_CDObjects
    

# -- PRESENTATION (Input/Output) -- #
class IO:

    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

        """
        choice = ''
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  
        return choice

    @staticmethod
    def show_inventory(lst_CDObjects):
        """Displays current inventory table

        Args:
            lst_CDObjects (list of objects): 2D data structure (list of CD objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')

        for row in lst_CDObjects:
            print('{}\t{} (by:{})'.format(row.cd_id, row.cd_title, row.cd_artist))
        print('======================================')
        
    @staticmethod
    def get_int_value(input_message, error_message):
        """ Prompts the user to enter an integer value

        Args:
            input_message (string): String presented to the user when prompting for data
            error_message (string): String presented to the user if bad data is entered

        Returns:
            int_id (int): Valid integer supplied by the user
        """

        while True:
            try:
                int_id = int(input(input_message).strip())
                return int_id
            except ValueError:
                print(error_message)
                
    @staticmethod
    def get_new_cd(listofIDs):
        """ Gets new CD information from the user

        Args:
             listofIDs(list): list containing the IDs in the current inventory

        Returns:
            intID (int): ID value for the new CD
            strTitle (string): Title of the new CD album
            strArtist (string): Artist of the new CD album
        """

     
        while True: 
            try:
                intID = IO.get_int_value("Enter ID: ", "This is not an integer value!")

                if intID in listofIDs:
                    raise IDAlreadyExistsError 
                strTitle = ''
                while strTitle == '':
                    strTitle = input('What is the CD\'s title? ').strip()
                strArtist = ''
                while strArtist == '':
                    strArtist = input('What is the Artist\'s name? ').strip()
                return intID, strTitle, strArtist
            except IDAlreadyExistsError: 
                print('That ID already exists \nEnter new ID')

    def get_current_IDs(lst_CDObjects):
        """ returns a list of IDs in the current inventory
        Args: 
            list_Inventory(list): list of CD objects containing CD information
        Returns:
            listofIds(list): list of IDs in the current inventory
        """
        listofIds = []
        for rows in lst_CDObjects:
            listofIds.append(rows.cd_id)
        return listofIds
    
    @staticmethod         
    def add_cd(cd_id, cd_title, cd_artist, lst_CDObjects):
        """ function to add a CD to the inventory
        Tells user to enter an integer if a value that cannot be type cast to 
        integer is entered

        Args:
            cd_id (int): ID value for the new CD 
            cd_title (string): Title of the new CD album
            cd_artist (string): Artist of the new CD album
            lst_CDObjects: the list of CDObjects containing the CD entries
            
        Returns: 
            the modified list of CD Objects with new etries of CDs
        """
       
        # Add item to the table
        newCDObj = CD(cd_id, cd_title, cd_artist)
        lst_CDObjects.append(newCDObj)
        return lst_CDObjects
    
    @staticmethod
    def delete_cd(lst_CDObjects, ID):
        """ function to delete an entry from the inventory
        
            Args:
                lst_CDObjects: the list of CD objects containing the CD entries
                ID: the integer ID of the CD to be deleted
                
            Returns: 
                the modified list of CD Objects with the object containing the ID removed
            """

        # search thru lst of CD Objects and delete CD
        intRowNr = -1
        blnCDRemoved = False
        for row in lst_CDObjects:
            intRowNr += 1
            if row.cd_id == ID:
                del lst_CDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return lst_CDObjects

class IDAlreadyExistsError(Exception):
    """ the ID already exists"""
    def __str__(self):
        return 'the ID already exists'


# -- Main Body of Script -- #
lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue 
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue        
    elif strChoice == 'a':
        idList = IO.get_current_IDs(lstOfCDObjects) 
        intID, strTitle, strArtist = IO.get_new_cd(idList)
        lstTbl = IO.add_cd(intID, strTitle, strArtist, lstOfCDObjects) 
        IO.show_inventory(lstOfCDObjects)  
        continue  
    elif strChoice == 'd':
        IO.show_inventory(lstOfCDObjects)
        intIDDel = IO.get_int_value("Please enter an ID to delete: ", "Please enter only an integer value.")
        lstOfCDObjects = IO.delete_cd(lstOfCDObjects, intIDDel) 
        IO.show_inventory(lstOfCDObjects)
        continue  
    elif strChoice == 's':
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  
    else:
        print('General Error')
        
        