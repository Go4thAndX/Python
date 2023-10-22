# De volgende code zou kunnen worden gebruikt om regels met cijfers van 0 tot 100 in verschillende rijen te creëren:

# for rij in range (1, 11): 
#     for cijfer in range (0, 101, 10): 
#         print (cijfer, end="\t")
#     print()
    
# Output:
# 0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49
# 50 51 52 53 54 55 56 57 58 59
# 60 61 62 63 64 65 66 67 68 69
# 70 71 72 73 74 75 76 77 78 79
# 80 81 82 83 84 85 86 87 88 89
# 90 91 92 93 94 95 96 97 98 99
# 100

# De volgende Python-code genereert regels met getallen die uit getallen bestaan van 0 tot en 100 in verschillende rijen, netjes uitgelijnd en met alle getallen evenveel karakters:
    
for i in range(101):
    print(f"{i:2d}", end=" ")
    if (i+1) % 10 == 0:
        print()
        
# Output:
#  0  1  2  3  4  5  6  7  8  9 
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49
# 50 51 52 53 54 55 56 57 58 59
# 60 61 62 63 64 65 66 67 68 69
# 70 71 72 73 74 75 76 77 78 79
# 80 81 82 83 84 85 86 87 88 89
# 90 91 92 93 94 95 96 97 98 99
# 100

# De volgende Python code genereert regels met getallen die uit getallen bestaan van 0 tot en met 100 in verschillende rijen netjes uitgeleind waarbij alle getallen ook nog uit even veel karakters bestaan dus 1 wordt  001 en 100 wordt 100 met python code

# for i in range(101):
#     print('{:03d}'.format(i), end=" ") 
#     if (i + 1) % 10 == 0: 
#         print()
        
# Output:
# 000 001 002 003 004 005 006 007 008 009 
# 010 011 012 013 014 015 016 017 018 019
# 020 021 022 023 024 025 026 027 028 029
# 030 031 032 033 034 035 036 037 038 039
# 040 041 042 043 044 045 046 047 048 049
# 050 051 052 053 054 055 056 057 058 059
# 060 061 062 063 064 065 066 067 068 069
# 070 071 072 073 074 075 076 077 078 079
# 080 081 082 083 084 085 086 087 088 089
# 090 091 092 093 094 095 096 097 098 099
# 100

# De volgende Python code genereert regels met getallen die uit getallen bestaan van 0 tot en met 100 in verschillende rijen netjes uitgeleind waarbij alle getallen ook nog uit even veel karakters bestaan dus 1 wordt  001 en 100 wordt 100 met python code en waarbij het aantal voorloopnullen afhankleijk is van de range

# range_start = 900
# range_end = 1000
# num_zeros = len(str(range_end))
# for i in range(range_start, range_end+1):
#     print('{:0{}d}'.format(i, num_zeros), end=" ") 
#     if (i + 1) % 10 == 0: 
#         print()
        
# Output:
# 0900 0901 0902 0903 0904 0905 0906 0907 0908 0909 
# 0910 0911 0912 0913 0914 0915 0916 0917 0918 0919
# 0920 0921 0922 0923 0924 0925 0926 0927 0928 0929
# 0930 0931 0932 0933 0934 0935 0936 0937 0938 0939
# 0940 0941 0942 0943 0944 0945 0946 0947 0948 0949
# 0950 0951 0952 0953 0954 0955 0956 0957 0958 0959
# 0960 0961 0962 0963 0964 0965 0966 0967 0968 0969
# 0970 0971 0972 0973 0974 0975 0976 0977 0978 0979
# 0980 0981 0982 0983 0984 0985 0986 0987 0988 0989
# 0990 0991 0992 0993 0994 0995 0996 0997 0998 0999
# 1000   
    