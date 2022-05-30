import input
import umrechnungen

def haupt():
    while True:
        s = input.Hauptmenü()
        if s == 1:
                s2 = input.Submenü()
                if s2 == 1:
                    print('Fehler')
                elif s2 == 2:
                    C = input.get_input_C()
                    umrechnungen.convert_CtoK(C)
                elif s2 == 3:
                    C = input.get_input_C()
                    umrechnungen.convert_CtoF(C)
                elif s2 == 4:
                    break
        elif s == 2:
                s2 = input.Submenü()
                if s2 == 1:
                    K = input.get_input_K()
                    umrechnungen.convert_KtoC(K)
                elif s2 == 2:
                    print('Fehler')
                elif s2 == 3:
                    K = input.get_input_K()
                    umrechnungen.convert_KtoF(K)
                elif s2 == 4:
                    break
        elif s == 3:
                s2 = input.Submenü()
                if s2 == 1:
                    F = input.get_input_F()
                    umrechnungen.convert_FtoC(F)
                elif s2 == 2:
                    F = input.get_input_F()
                    umrechnungen.convert_FtoK(F)
                elif s2 == 3:
                    print('Fehler')
                elif s2 == 4:
                    break
        elif s == 4:
            break
    
haupt()


#'''if __name__ == "__ma n__":
    #C = input.get_input_C()
   # '''if C == 'exit' or 'Exit':
   #     print(C)
    #else:'''
    #umrechnungen.convert_CtoK(C)'''
