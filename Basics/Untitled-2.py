#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Basics'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ## Strings ("meh")"
#%% [markdown]
# Me: Do I have to do this ?
# Instructor: Yes.
# Me: But I know programming fundamentals, I know java!
# Instructor: baby steps bro baby steps.
#%% [markdown]
# just shifting my lingo from java to python
#%% [markdown]
# Here we do print, slicing, stringing(variables), etc, length, etc  __Remember in code indexing starts at 0__  :rocket:

#%%
"Sup' Boi ?"


#%%
print("'Sup \n Boi ?'")


#%%
str = "Sup' Boi ?"


#%%
print(str)


#%%
str[0]

#%% [markdown]
# __Reverse Indexing__ 

#%%
str[-2]


#%%
str[-5]


#%%
str[-1]

#%% [markdown]
# -1 returns last chr of the string __Sup' Boi ?__
#%% [markdown]
# __SLICING__

#%%
str1 = "madhavshekharsharma"


#%%
str1


#%%
str1[6:]

#%% [markdown]
# from what index you wanna slice__:__till where you wanna slice

#%%
str1[:6]


#%%
str1[6:13]


#%%
str1[::2]

#%% [markdown]
# Here 2 is rep of __step size__ i.e go in jumps of __2__
#%% [markdown]
# ##### Found A Wonderful Trick
# To reverse a string using slicing and using step count as -1 <br>
# __insert HACKERMAN meme here__

#%%
str1[::-1]

#%% [markdown]
# ### STRING ENDGAME
# 1. Strings are immutable
# 2. String Methods

#%%
# str[1] = 'K'

#%% [markdown]
# strings immutable therefore this returns an error<br>does not support item assignment<br>
# __Explaination__: Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)
#%% [markdown]
# therefore to change a chr we have to use concatenation<br> __Example below__

#%%
str2 = "Tony Stark"

#%% [markdown]
# __AIM:__ To change Tony Stark to Arya Stark

#%%
str3 = str2[4:]


#%%
print(str3)


#%%
print("Arya" + str3)

#%% [markdown]
# _Voila!_<br>
# __P.S:__ We can also concatenate using muliplication i.e __*__
#%% [markdown]
# ###### Callback to python's Dynamic Typing feature

#%%
7 + 8


#%%
'7' + '8'

#%% [markdown]
# ### 2. String Methods
# Methods discussed here are:
# * .upper() : __obvio__
# * .lower() : __obvio__
# * .split() : __splits the string into words and stores it in a list__ (breaks at blank spaces or anything we specify on)

#%%
str4 = "Steve Rogers"


#%%
str4.upper()


#%%
str4.lower()


#%%
str4.split()


#%%
str4.split('e')


#%%
str4encoded = str4.encode("ascii", "ignore")


#%%
print("Original String: " + str4)

#%% [markdown]
# 
#%% [markdown]
# 
#%% [markdown]
# # # String Formatting
#  
#  String formatting lets you inject items into a string rather than trying to chain items together using commas or string concatenation. As a quick comparison, consider:
# 
#      player = 'Thomas'
#      points = 33
#      
#      'Last night, '+player+' scored '+str(points)+' points.'  # concatenation
#      
#      f'Last night, {player} scored {points} points.'          # string formatting
#  
#  
#  There are three ways to perform string formatting.
#  * The oldest method involves placeholders using the modulo `%` character.
#  * An improved technique uses the `.format()` string method.
#  * The newest method, introduced with Python 3.6, uses formatted string literals, called *f-strings*.
#%% [markdown]
# ## Formatting with the `.format()` method
# A better way to format objects into your strings for print statements is with the string `.format()` method. The syntax is:
#  
#      'String here {} then also {}'.format('something1','something2')
#      
#  For example:

#%%
print('The {} {} {}'.format('fox','brown','quick'))

#%% [markdown]
# #### 1. Inserted objects can be called by index position:

#%%
print('The {2} {1} {0}'.format('fox','brown','quick'))

#%% [markdown]
# #### 2. Inserted objects can be assigned keywords:

#%%
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))

#%% [markdown]
# #### 3. Inserted objects can be reused, avoiding duplication:

#%%
print('A %s saved is a %s earned.' %('penny','penny'))
# vs.
print('A {p} saved is a {p} earned.'.format(p='penny'))


#%%



