import urllib.request
import re
from bs4 import BeautifulSoup

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def extract_text():
	text = 'JZFC XLUPDEJ,TE SLD MPPY XJ OPPAPDE AWPLDFCP LYO L RCPLE ACTGTWPRP EZ DPCGP LD JZF ACTGLEP DPNCPELCJ ESPDP WLDE YTYP JPLCD, LYO ESZFRS TE HZFWO MP XJ LCOPYE HTDS EZ NZYETYFP EZ DPCGP JZF ESCZFRSZFE JZFC CPTRY, HP LCP, YZYP ZQ FD, TXXZCELW, LYO XJ ESZFRSED SLGP EFCYPO EZ XJ DFNNPDDZC.JZF LCP ZQ NZFCDP PYETEWPO EZ OTDCPRLCO XJ LOGTNP, SZHPGPC T SLGP RTGPY NZYDTOPCLETZY EZ ESP NSLYRPD TY XJ CZWP ZGPC ESP WLDE DPGPCLW JPLCD. LD JZFC PXATCP SLD RCZHY TY XLRYTQTNPYNP, ZESPCD LNCZDD ZFC NZYETYPYE SLGP RCZHY QCLNETZFD, LYO LY TYNCPLDTYR AZCETZY ZQ XJ ETXP TD DAPYE XLYLRTYR ESP TXALNE ZQ ESPTC BFLCCPWD FAZY ZFC TDWLYO. T SLGP QPWE, LE ETXPD, WTVP DEPASPYDZY’D OC UPVJWW LD T SLGP XLYLRPO JZFC SZFDPSZWO LQQLTCD LYO ESP XZCP AFMWTN LDAPNED ZQ JZFC DELEP. LE ZESPCD T SLGP MPPY ACPDDPO EZ FYOPCELVP ESP CZWP ZQ XC SJOP, QZNFDDTYR XJ CLRP FYOPC RCPLE ACZGZNLETZY QCZX ESP AZHPCD ESLE ESCPLEPY EZ LDDLTW FD. HTES ESPDP CPQWPNETZYD T SLGP NZXP EZ ESP GTPH ESLE ESP ETXP XLJ SLGP NZXP EZ OTDDPNE ESP CZWP ZQ ACTGLEP DPNCPELCJ TYEZ TED EHZ GPCJ DPALCLEP QFYNETZYD.ESP AFMWTN QLNP ZQ ESP CZJLW SZFDPSZWO XFDE ZQ NZFCDP NZYETYFP EZ MP ACPDPYEPO MJ DZXPZYP ZQ RCLNP LYO OTRYTEJ HSZ NLY NZXXLYO ESP NZYQTOPYNP ZQ ESP NZFCETPCD. HP SLGP OTDNFDDPO LE WPYRES HSZ XTRSE QTWW ESLE CZWP HSPY T PGPYEFLWWJ ALDD ZY, LYO T MPWTPGP ESLE HP SLGP LRCPPO EZ TYGTEP AZYDZYMJ EZ TYSPCTE ESLE XLYEWP. SP TD L RZZO XLY LYO HTWW DPCGP JZF HPWW. T HZFWO DFRRPDE ESLE QZC ESP DLVP ZQ NZYETYFTEJ SP NZYETYFPD EZ NLCCJ ESP ETEWP ZQ ACTGLEP DPNCPELCJ LYO HTWW MP SLAAJ EZ ACPALCP STX QZC ESTD CZWP. SZHPGPC ESPCP LCP DZXP LDAPNED ZQ XJ LNETGTETPD ESLE T DFDAPNE ESLE AZYDZYMJ HZFWO DECFRRWP EZ LNNZXAWTDS LYO QZC ESZDP T HZFWO TYGTEP JZF EZ NZYDTOPC L YPH AZDTETZY TY JZFC SZFDPSZWO, ESLE ZQ DPNCPE DPNCPELCJ.TY ESPDP BFLCCPWDZXP ETXPD TE XLJ MP YPNPDDLCJ EZ NZXXTDDTZY LNETZYD ZC PYBFTCTPD ESLE DZXP XTRSE CPRLCO LD MPYPLES ESP OTRYTEJ ZQ ESP NCZHY. ESP DPNCPE DPNCPELCJ NLY, MJ NZYNPLWTYR ESPDP LNETGTETPD, ACPDPCGP ESP CPAFELETZY ZQ JZFC RZGPCYXPYE LD L CPWTLMWP LYO ECFDEHZCESJ ALCETNTALYE TY TYEPCYLETZYLW LQQLTCD, HSTWP LWDZ ACZGTOTYR JZF LYO JZFC XTYTDEPCD HTES ESP HPLAZYD EZ OPQPLE ZFC PYPXTPD. TQ HP DFNNPPO LD T SZAP HP HTWW, ESPY HLCD ZQ ESP QFEFCP XLJ MP HZY HTESZFE L DSZE MPTYR QTCPO.TE TD XJ QPCGPYE SZAP ESLE JZF LRCPP HTES XJ LYLWJDTD LYO ESLE EZRPESPC HP NLY XZGP EZ PDELMWTDS ESP YPH ZQQTNP. T SLGP DPGPCLW YLXPD ESLE T HZFWO SFXMWJ DFRRPDE LD DECZYR NLYOTOLEPD QZC ESP YPH CZWP. LWW LCP RZZO XPY, HTES XTWTELCJ MLNVRCZFYOD LYO L CPAFELETZY QZC SZYZFC ESLE YZ-ZYP NZFWO BFPDETZY. T HTWW MP SLAAJ EZ OTDNFDD ESTD QFCESPC LE JZFC AWPLDFCP.JZFC QLTESQFW DPCGLYE,NSLCWPD RCPJ'
	return text

def frequency(text):
	freq_character = []
	#text = extract_text()
	for j in alphabet:
		result = re.findall(j, text)
		freq_character.append(len(result))
	probability=[]
	PlainText = re.sub(r'\W', '', text)
	total_cahracter = len(PlainText)
	for each in freq_character:
		probability.append(int(each)/total_cahracter)
	#print(probability)
	return probability

def guessing(text):
	text = re.sub(r'[^\w\s]','',text)
	text = text.split(' ')
	#for each in text:
	#	if len(each) == 3:


def dictionary():
	pass

def x_plus_a_check(index_e, index_t):
	if index_e > 4:
		a = 26 - (index_e - 4)
	else:
		a = 4 - index_e
	if (index_t + a)%26 == 19: #check with t
		return a
	else:
		return False

def x_plus_a(index_e, index_t):
	mapping = []
	a = x_plus_a_check(index_e, index_t)
	for i in range(0, 26):
		alphabet_position = (i + a)%26
		mapping.append([alphabet[i], alphabet[alphabet_position]]) #[encrypt, decrypt]
	#print(mapping)
	return mapping
	
def ax_plus_b_check(index_e, index_t):
	#[m, m']
	check = []
	modulus_inverse = [[1, 1], [3, 9], [5, 21], [7, 15], [9, 3], [11, 19], [15, 7], [17, 23], [19, 11], [21, 5], [23, 17], [25, 25]]
	m = abs(index_e - index_t)
	for each in modulus_inverse:
		if each[0] = m:
			m_inverse = each[1]
			check.append(1)
		else:
			pass
	if len(check) == 1:
		if index_e > index_t:
			a = ((-15)*m_inverse)%26
		else:
			a = (15*m_inverse)%26
		b = (4 - index_e*a)%26
		return a,b
	else:
		return False

def ax_plus_b(index_e, index_t):
	mapping = []
	a, b = ax_plus_b_check(index_e, index_t)[0], ax_plus_b_check(index_e, index_t)[1]
	for i in range(0, 26):
		alphabet_position = ((a*i + b))%26
		mapping.append([alphabet[i]], alphabet[alphabet_position]) #[encrypt, decrypt]
	#print(mapping)
	return mapping

def transposition():
	pass

def decrypt():
	text = extract_text()
	probability = frequency(text)
	letter_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
					0.00153, 0.0772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01925, 0.0095, 
					0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
	maximum_e = max(probability)
	index_e = probability.index(maximum_e)
	maximum_t = sorted(probability)[-2]
	index_t = probability.index(maximum_t)
	if alphabet[index_e] != 'E':
		if maximum_e >= 0.108 and maximum_t >= 0.087:
			if x_plus_a_check(index_e, index_t):
				for each in x_plus_a(index_e, index_t):
					old, new = each[0], str.lower(each[1])
					text = re.sub(old, new, text)
			elif ax_plus_b_check(index_e, index_t):
				for each in ax_plus_b(index_e, index_t):
					old, new = each[0], str.lower(each[1])
					text = re.sub(old, new, text)
			else: #maybe guessing or dictionary
				print('iii')
		elif maximum_e >= 0.11 and maximum_t <= 0.087:
			text = re.sub(alphabet[index_e], 'E', text)
		else:
			pass
	else:
		transposition()
	
	#print(text)

if __name__ == '__main__':
	decrypt()
	#x_plus_a_check(15, 4)
	#x_plus_a(15, 4)