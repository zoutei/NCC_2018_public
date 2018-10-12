bigrams = [["th", 1.52],["he", 1.28],["in", 0.94],["er", 0.94],["an", 0.82],["re", 0.68],["nd", 0.63],["at", 0.59],["on", 0.57],["nt", 0.56],["ha", 0.56],["es", 0.56],["st", 0.55],["en", 0.55],["ed", 0.53],["to", 0.52],["it", 0.50],["ou", 0.50],["ea", 0.47],["hi", 0.46],["is", 0.46],["or", 0.43],["ti", 0.34],["as", 0.33],["te", 0.27],["et", 0.19],["ng", 0.18],["of", 0.16],["al", 0.09],["de", 0.09],["se", 0.08],["le", 0.08],["sa", 0.06],["si", 0.05],["ar", 0.04],["ve", 0.04],["ra", 0.04],["ld", 0.02],["ur", 0.02]]

def removespace(text):
    textnospace = []
    for c in text:
        if c != ' ' or c != '.':
            textnospace.append(c)
    return textnospace

def countbigram(text):
    bigram_count = [0] * len(bigrams)
    for i in range(len(text)-2):
        chars = text[i] + text[i+1]
        for j in range(len(bigrams) - 1):
            if chars == bigrams[j][0]:
                bigram_count[j] += 1
    return bigram_count

def checkenglishnes(text):
    score = 0

    return score

if __name__ == '__main__':
    text = "life had been relatively dull since returning from my work with harry in the middle east. the british library was delighted to get its hands on the roman diary and the collector seemed to have forgotten about me maybe because harrys team made it too dangerous to hang around. i was happy to settle back in to my work at the library and was involved in a project to track down and catalogue missing documents from the late nineteenth century. they detailed foreign policy which sounds dull but with victoria taking an active interest there were a lot of letters between downing street and the palace and i was enjoying spying on famous characters from history. i really felt like i was getting some insight into how they thought and how the modern world came into being in that tumultuous period. while i was mainly there to check the letters for authenticity i got really involved in trying to understand how they all fitted together and part of the job was to cross check statements in the letters with what we know actually happened. there are a lot of people who will pay a lot of money to own a letter from a royal so the archive is plagued with forgeries. some of them you can detect by analysing the paper others by the writing style. some just fall over because the content is out of line with other documents but as i studied them i began to realise that a number of them hinted at events that i couldnt find in the historical record. certain names appeared and were clearly important and then disappeared completely from trace. diplomatic incidents were mentioned that never happened according to the history books. one thing you learn in this business is that the civil service never lets any decision however secret go unrecorded. of course that might just have meant those letters and documents were fake but i pride myself on being an excellent forger and i would not have been able to produce them. the paper was right the ink was chemically correct and aged just the right amount and the style of writing was totally convincing. and i was convinced. convinced that somewhere there must be an archive of government documents from the period that recorded all of these missing stories in full. then i received the message about the shadow archive someone else knew about it and had worked out that i was hunting for it too the postcard didnt help much but the emails did the first one had the subject line jekyll and hyde and was encrypted using a simple caesar shift to discourage casual interest it didnt take me long to crack it and the names and details it contained matched the growing list of mysterious references from my own research douglas black was clearly an important figure and i had a feeling that he had something to do with the archive that feeling was confirmed by the second email black heart that i received later that week again it was encrypted but this time using an affine shift cipher it was clearly from the same individual  at the very least whoever was sending me the emails had a habit of missing the letter r from the word your someone was playing games with me and i was more than happy to join in"
    print(countbigram(removespace(text)))
