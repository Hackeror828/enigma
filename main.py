print("""
                                                                           
                        ,--.                              ____             
   ,---,              ,--.'|   ,---,  ,----..           ,'  , `.    ,---,. 
  '  .' \         ,--,:  : |,`--.' | /   /   \       ,-+-,.' _ |  ,'  .' | 
 /  ;    '.    ,`--.'`|  ' :|   :  :|   :     :   ,-+-. ;   , ||,---.'   | 
:  :       \   |   :  :  | |:   |  '.   |  ;. /  ,--.'|'   |  ;||   |   .' 
:  |   /\   \  :   |   \ | :|   :  |.   ; /--`  |   |  ,', |  '::   :  |-, 
|  :  ' ;.   : |   : '  '; |'   '  ;;   | ;  __ |   | /  | |  ||:   |  ;/| 
|  |  ;/  \   \'   ' ;.    ;|   |  ||   : |.' .''   | :  | :  |,|   :   .' 
'  :  | \  \ ,'|   | | \   |'   :  ;.   | '_.' :;   . |  ; |--' |   |  |-, 
|  |  '  '--'  '   : |  ; .'|   |  ''   ; : \  ||   : |  | ,    '   :  ;/| 
|  :  :        |   | '`--'  '   :  |'   | '/  .'|   : '  |/     |   |    \ 
|  | ,'        '   : |      ;   |.' |   :    /  ;   | |`-'      |   :   .' 
`--''          ;   |.'      '---'    \   \ .'   |   ;/          |   | ,'   
               '---'                  `---`     '---'           `----'     
                                                                           
""")
print("""
+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+
|m|a|d|e| |b|y| |H|A|C|K|E|R|O|R|8|2|8|
+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+
""")


print ("Do you want to encrypt or decrypt ?")
while True:
    use = input("Choose an option (1, 2), or type 'exit' to quit: ")
    if use == 'exit':
        print("Bye!")
        break
    elif use == "1":
        print('encrypt.')
        import anigma_1
        anigma_1.main()
        break
    elif use == "2":  # Fixed the indentation here
        print('decrypt.')
        import decrypt
        decrypt.main()
        break
    else:
        print("Invalid choice. Please choose a valid option.")
        continue
