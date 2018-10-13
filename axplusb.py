import re
from checkenglishness import *

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_map_of_x_plus_a(a):
    mapping = []
    for i in range(26):
        alphabet_position = (i + a) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    return mapping

def ax_plus_b_check(index_e, index_t):
    # [m, m']
    check = []
    modulus_inverse = [[1, 1], [3, 9], [5, 21], [7, 15], [9, 3], [11, 19], [15, 7], [17, 23], [19, 11], [21, 5],
                       [23, 17], [25, 25]]
    m = abs(index_e - index_t)
    for each in modulus_inverse:
        if each[0] == m:
            m_inverse = each[1]
            check.append(1)
        else:
            pass
    if len(check) == 1:
        if index_e > index_t:
            a = ((-15) * m_inverse) % 26
        else:
            a = (15 * m_inverse) % 26
        b = (4 - index_e * a) % 26
        return a, b
    else:
        return False

def get_map_of_ax_plus_b(a, b):
    mapping = []
    for i in range(0, 26):
        alphabet_position = (a * i + b) % 26
        mapping.append([alphabet[i], alphabet[alphabet_position]])  # [encrypt, decrypt]
    return mapping

def decrypt(text, mapping):
    for each in mapping:
        old, new = each[0], str.lower(each[1])
        text = re.sub(old, new, text)
    return text

if __name__ == '__main__':
    #x+a
    text = "AOL ZPNUZ DLYL ZBIASL, HUK PA AVVR TL H DOPSL AV ZWVA AOLT, IBA NYHKBHSSF P ZAHYALK AV THRL AOLT VBA, HUK SPRL VUL VM AOVZL VSK MHZOPVULK 3K WPJABYLZ, AOHA ZWYPUNZ PUAV MVJBZ DOLU FVB JYVZZ FVBY LFLZ HUK JVBUA AV H OBUKYLK, AOL AYBAO JYFZAHSSPZLK HUK P YLHSPZLK AOHA P OHK ILLU ZLHYJOPUN MVY PA HSS HSVUN. PA DHZU’A AOHA P MVBUK ZVTLAOPUN WHYAPJBSHY. DOHA P UVAPJLK DHZ HJABHSSF HU HIZLUJL, H DOVSL JVSSLJAPVU VM HWWHYLUASF BUYLSHALK AOPUNZ AOHA ZOVBSK OHCL LEPZALK IBA KPKU’A. HUK QBZA HZ P OHK MPNBYLK AOHA VBA, ZVTLVUL, HUK IHJR AOLU P KPKU’A RUVD DOV, DYVAL AV ALSS TL HIVBA PA. AOLF VICPVBZSF OHK H ZLUZL VM AOL KYHTHAPJ, HUK HU LEJLSSLUA ZLUZL VM APTPUN. PM AOLF OHK ZLUA PA AV TL LCLU H MLD KHFZ ILMVYL P DVBSK OHCL HZZBTLK PA DHZ ZVTL RPUK VM JYHGF HKCLYAPZPUN ZABUA, IBA DOLU AOL WVZAJHYK HYYPCLK, PA DHZ PTTLKPHALSF VICPVBZ AV TL DOHA PA YLMLYYLK AV. PA JHYYPLK QBZA AOYLL DVYKZ, HUK PA KLZJYPILK WLYMLJASF AOL TPZZPUN WPLJLZ PU TF WBGGSL. PA QBZA ZHPK: AOL ZOHKVD HYJOPCL."
    for a in range(26):
        text_decrypted = decrypt(text, get_map_of_x_plus_a(a))
        score = get_english_score(text_decrypted)
        print(score)

    #ax+b
    a_possible = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    text = "JZFC XLUPDEJ, TE SLD MPPY XJ OPPAPDE AWPLDFCP LYO L RCPLE ACTGTWPRP EZ DPCGP LD JZF ACTGLEP DPNCPELCJ ESPDP WLDE YTYP JPLCD, LYO ESZFRS TE HZFWO MP XJ LCOPYE HTDS EZ NZYETYFP EZ DPCGP JZF ESCZFRSZFE JZFC CPTRY, HP LCP, YZYP ZQ FD, TXXZCELW, LYO XJ ESZFRSED SLGP EFCYPO EZ XJ DFNNPDDZC. JZF LCP ZQ NZFCDP PYETEWPO EZ OTDCPRLCO XJ LOGTNP, SZHPGPC T SLGP RTGPY NZYDTOPCLETZY EZ ESP NSLYRPD TY XJ CZWP ZGPC ESP WLDE DPGPCLW JPLCD. LD JZFC PXATCP SLD RCZHY TY XLRYTQTNPYNP, ZESPCD LNCZDD ZFC NZYETYPYE SLGP RCZHY QCLNETZFD, LYO LY TYNCPLDTYR AZCETZY ZQ XJ ETXP TD DAPYE XLYLRTYR ESP TXALNE ZQ ESPTC BFLCCPWD FAZY ZFC TDWLYO. T SLGP QPWE, LE ETXPD, WTVP DEPASPYDZY’D OC UPVJWW LD T SLGP XLYLRPO JZFC SZFDPSZWO LQQLTCD LYO ESP XZCP AFMWTN LDAPNED ZQ JZFC DELEP. LE ZESPCD T SLGP MPPY ACPDDPO EZ FYOPCELVP ESP CZWP ZQ XC SJOP, QZNFDDTYR XJ CLRP FYOPC RCPLE ACZGZNLETZY QCZX ESP AZHPCD ESLE ESCPLEPY EZ LDDLTW FD. HTES ESPDP CPQWPNETZYD T SLGP NZXP EZ ESP GTPH ESLE ESP ETXP XLJ SLGP NZXP EZ OTDDPNE ESP CZWP ZQ ACTGLEP DPNCPELCJ TYEZ TED EHZ GPCJ DPALCLEP QFYNETZYD. ESP AFMWTN QLNP ZQ ESP CZJLW SZFDPSZWO XFDE ZQ NZFCDP NZYETYFP EZ MP ACPDPYEPO MJ DZXPZYP ZQ RCLNP LYO OTRYTEJ HSZ NLY NZXXLYO ESP NZYQTOPYNP ZQ ESP NZFCETPCD. HP SLGP OTDNFDDPO LE WPYRES HSZ XTRSE QTWW ESLE CZWP HSPY T PGPYEFLWWJ ALDD ZY, LYO T MPWTPGP ESLE HP SLGP LRCPPO EZ TYGTEP AZYDZYMJ EZ TYSPCTE ESLE XLYEWP. SP TD L RZZO XLY LYO HTWW DPCGP JZF HPWW. T HZFWO DFRRPDE ESLE QZC ESP DLVP ZQ NZYETYFTEJ SP NZYETYFPD EZ NLCCJ ESP ETEWP ZQ ACTGLEP DPNCPELCJ LYO HTWW MP SLAAJ EZ ACPALCP STX QZC ESTD CZWP. SZHPGPC ESPCP LCP DZXP LDAPNED ZQ XJ LNETGTETPD ESLE T DFDAPNE ESLE AZYDZYMJ HZFWO DECFRRWP EZ LNNZXAWTDS LYO QZC ESZDP T HZFWO TYGTEP JZF EZ NZYDTOPC L YPH AZDTETZY TY JZFC SZFDPSZWO, ESLE ZQ DPNCPE DPNCPELCJ. TY ESPDP BFLCCPWDZXP ETXPD TE XLJ MP YPNPDDLCJ EZ NZXXTDDTZY LNETZYD ZC PYBFTCTPD ESLE DZXP XTRSE CPRLCO LD MPYPLES ESP OTRYTEJ ZQ ESP NCZHY. ESP DPNCPE DPNCPELCJ NLY, MJ NZYNPLWTYR ESPDP LNETGTETPD, ACPDPCGP ESP CPAFELETZY ZQ JZFC RZGPCYXPYE LD L CPWTLMWP LYO ECFDEHZCESJ ALCETNTALYE TY TYEPCYLETZYLW LQQLTCD, HSTWP LWDZ ACZGTOTYR JZF LYO JZFC XTYTDEPCD HTES ESP HPLAZYD EZ OPQPLE ZFC PYPXTPD. TQ HP DFNNPPO LD T SZAP HP HTWW, ESPY HLCD ZQ ESP QFEFCP XLJ MP HZY HTESZFE L DSZE MPTYR QTCPO. TE TD XJ QPCGPYE SZAP ESLE JZF LRCPP HTES XJ LYLWJDTD LYO ESLE EZRPESPC HP NLY XZGP EZ PDELMWTDS ESP YPH ZQQTNP. T SLGP DPGPCLW YLXPD ESLE T HZFWO SFXMWJ DFRRPDE LD DECZYR NLYOTOLEPD QZC ESP YPH CZWP. LWW LCP RZZO XPY, HTES XTWTELCJ MLNVRCZFYOD LYO L CPAFELETZY QZC SZYZFC ESLE YZ-ZYP NZFWO BFPDETZY. T HTWW MP SLAAJ EZ OTDNFDD ESTD QFCESPC LE JZFC AWPLDFCP. JZFC QLTESQFW DPCGLYE, NSLCWPD RCPJ"
    for a in a_possible:
        for b in range(26):
            text_decrypted = decrypt(text, get_map_of_ax_plus_b(a, b))
            score = get_english_score(text_decrypted)
            print(score)