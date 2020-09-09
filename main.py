'''
# 8-1 : Message

def display_message():
    print("We are going to learn about functions in this chapter!")


display_message()
print('\n')


# 8-2 : Favorite book

def favorite_book(bookTitle):
    print("One of my favorite books is", bookTitle)


favorite_book("Python Crash Course")


# 8-3 : T-Shirt

def make_shirt(size, text):
    print(" The size of the shirt is", size)
    print('\'', text, '\'', "will be printed on your t-shirt")


make_shirt("XL", "I'm a foodie")
make_shirt(text="I love food", size="L")  # when using keyword arguments, the order does not matter

# 8-4 : Large shirt

print('\n')


def modi_make_shirt(size="L", text="I love Python"):
    print(" The size of the shirt is", size)
    print('\'', text, '\'', "will be printed on your t-shirt")


modi_make_shirt()
modi_make_shirt(size='M')
modi_make_shirt(size='XS', text="You Can Do it!")

print('\n')


# 8-5 Cites

def describe_city(city, country="S.Korea"):
    print(city.title(), "is in", country.title())


describe_city("gyeongju")
describe_city("phohang")
describe_city("paris", "france")
describe_city("san francisco", country="U.S.A")

print('\n')


# 8-6 City Names

def city_country(city_n, country_n):
    formatted = '\"' + city_n.title() + ", " + country_n.title() + '\"'
    return formatted


cityNcountry = city_country("san jose", "United States")
print(cityNcountry)


# 8-7 : Album
def make_album(artist, albumtitle, numOftrack=0):
    albumInfo = {'Artist Name': artist, 'Album Title': albumtitle}
    if numOftrack:
        albumInfo['Number of Track'] = numOftrack
    return albumInfo


album = make_album("BTS", "Boy with luv")
print(album)

album2 = make_album("Hasley", "You should be sad", 5)
print(album2)

album3 = make_album("Justin bieber", " Sorry")
print(album3)

# 8-8

while True:
    print("Press 'q' to quit")

    userN = input("Please enter the name of the artist:")
    userT = input("Please enter the title of the album:")


    if userN == 'q':
        break
    if userT == 'q':
        break

    userAlbum = make_album(userN,userT)
    print(userAlbum)
    print('\n')

#8-9 : Magicians

#this functions prints the name of magicians
def show_magicians(m_list):
    for name in m_list:
        print(name.title())

magicians =["Brian", "bob", "sunny","jack","charles"]

print("This is the name of magicians in the list")
show_magicians(magicians)


#8-10 : Great Magicians

def show_magicians(m_list):
    for name in m_list:
        print(name.title())

def make_great(m_list,greatM_list):
    while m_list:
        curr = "The Great " + m_list.pop()
        greatM_list.append(curr)

magicians = ["Brian", "bob", "sunny", "jack", "charles"]
great_magicians = []
print("This is the name of magicians in the list")

show_magicians(magicians) #before adding the great to each magician's name
make_great(magicians,great_magicians)
show_magicians(great_magicians)#After adding the great
'''
#8-11 : Unchanged Magicians

def show_magicians(m_list):
    for name in m_list:
        print(name.title())

def make_great(m_list,greatM_list):
    while m_list:
        curr = "The Great " + m_list.pop()
        greatM_list.append(curr)

    return m_list

magicians = ["Brian", "bob", "sunny", "jack", "charles"]
great_magicians = []
print("This is the name of magicians in the list")
show_magicians(magicians) #before adding the great to each magician's name
make_great(magicians[:],great_magicians)
show_magicians(great_magicians)
print("\nOriginal names:")
show_magicians(magicians)
