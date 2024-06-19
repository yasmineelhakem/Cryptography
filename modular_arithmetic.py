print(pow(11, 1, 6))
print(pow(8146798528947, 1, 17))
print(pow(273246787654, 65536, 65537))

"""  The modular multiplicative inverse of an integer 
For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p
                                                                              g=d^-1 mod p """
# What is the inverse element: 3 * d ≡ 1 mod 13?
from Crypto.Util.number import inverse
d = inverse(3, 13)
print(d)

"""          Quadratic Residu
We say that an integer x is a Quadratic Residue if there exists an a such that a^2 = x mod p. 
If there is no such solution, then the integer is a Quadratic Non-Residue.
wel a yetsama square root 
"""
from sympy.ntheory import is_quad_residue, sqrt_mod
print(is_quad_residue(14, 29))
print(is_quad_residue(6, 29))
print(is_quad_residue(11, 29))

#taw naarfou eli 6 houwa quadratic residu bech ntal3ou square root
print(sqrt_mod(6, 29))

""" p gets larger, this method becomes wildly unreasonable.
=> we have a way to check whether an integer is a quadratic residue with a single calculation 
thanks to       Legendre    

Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue

p odd prime
Legendre's Symbol: (a / p) ≡ a*((p-1)/2) mod p
=> (a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p
   (a / p) = -1 if a is a quadratic non-residue mod p
   (a / p) = 0 if a ≡ 0 mod p
=> calculating pow(a,(p-1)//2,p) is enough to determine if a is a quadratic residue

"""
from sympy import legendre_symbol
p = 101524035174539890485408575671085261788758965189060164484385690801466167356667036677932998889725476582421738788500738738503134356158197247473850273565349249573867251280253564698939768700489401960767007716413932851838937641880157263936985954881657889497583485535527613578457628399173971810541670838543309159139
ints = [25081841204695904475894082974192007718642931811040324543182130088804239047149283334700530600468528298920930150221871666297194395061462592781551275161695411167049544771049769000895119729307495913024360169904315078028798025169985966732789207320203861858234048872508633514498384390497048416012928086480326832803, 45471765180330439060504647480621449634904192839383897212809808339619841633826534856109999027962620381874878086991125854247108359699799913776917227058286090426484548349388138935504299609200377899052716663351188664096302672712078508601311725863678223874157861163196340391008634419348573975841578359355931590555, 17364140182001694956465593533200623738590196990236340894554145562517924989208719245429557645254953527658049246737589538280332010533027062477684237933221198639948938784244510469138826808187365678322547992099715229218615475923754896960363138890331502811292427146595752813297603265829581292183917027983351121325, 14388109104985808487337749876058284426747816961971581447380608277949200244660381570568531129775053684256071819837294436069133592772543582735985855506250660938574234958754211349215293281645205354069970790155237033436065434572020652955666855773232074749487007626050323967496732359278657193580493324467258802863, 4379499308310772821004090447650785095356643590411706358119239166662089428685562719233435615196994728767593223519226235062647670077854687031681041462632566890129595506430188602238753450337691441293042716909901692570971955078924699306873191983953501093343423248482960643055943413031768521782634679536276233318, 85256449776780591202928235662805033201684571648990042997557084658000067050672130152734911919581661523957075992761662315262685030115255938352540032297113615687815976039390537716707854569980516690246592112936796917504034711418465442893323439490171095447109457355598873230115172636184525449905022174536414781771, 50576597458517451578431293746926099486388286246142012476814190030935689430726042810458344828563913001012415702876199708216875020997112089693759638454900092580746638631062117961876611545851157613835724635005253792316142379239047654392970415343694657580353333217547079551304961116837545648785312490665576832987, 96868738830341112368094632337476840272563704408573054404213766500407517251810212494515862176356916912627172280446141202661640191237336568731069327906100896178776245311689857997012187599140875912026589672629935267844696976980890380730867520071059572350667913710344648377601017758188404474812654737363275994871, 4881261656846638800623549662943393234361061827128610120046315649707078244180313661063004390750821317096754282796876479695558644108492317407662131441224257537276274962372021273583478509416358764706098471849536036184924640593888902859441388472856822541452041181244337124767666161645827145408781917658423571721, 18237936726367556664171427575475596460727369368246286138804284742124256700367133250078608537129877968287885457417957868580553371999414227484737603688992620953200143688061024092623556471053006464123205133894607923801371986027458274343737860395496260538663183193877539815179246700525865152165600985105257601565]
for a in ints:
    legendre_value = legendre_symbol(a, p) #calculates q/p
    if legendre_value == 1:
        res = a
        break
print(res)
#we have hint p = 3 mod(4)
print(pow(res, (p+1)//4, p)) # ama mafhmtch aleh hedhi shiha
print(sqrt_mod(res, p)) # http://www.numbertheory.org/php/tonelli.php  site hedha ata nafs res hedhi

"""     Tonelli Shanks
In a congruence of the form r^2 ≡ a mod p, Tonelli-Shanks calculates r.
Tonelli-Shanks doesn't work for composite (non-prime) moduli. 
lezem l p prime + odd

yaani p = legen3 mod(4)
ou p = 1 mod(4)

"""

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

def tonelli_shanks(p, n):
    # Case when p|n, so n=0(mod p). The square root of 0 is 0.
    if n % p == 0:
        return 0

    # So we can assume n is coprime to p, i.e. p does not divide n.
    # Use Euler's criteria to see if a solution exists or not
    if not is_quad_residue(n, p):
        print("This value of n is not a quadratic residue.")
        return None
    else:
        print("This value of n is a quadratic residue.")

    # If p=3(mod 4) and we know n is a quadratic residue then
    # we can solve x^2=n(mod p) directly
    if p % 4 == 3:
        return pow(n, (p + 1)//4, p)

    # So now p=1(mod 4), (although this is not needed in the algorithm).
    # Write p - 1 = (2^S)(Q) where Q is odd
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        S += 1
        Q //= 2
    print("Q=", Q)
    print("S=", S)

    # Find a quadratic non-residue of p by brute force search
    z = 2
    while is_quad_residue(z, p):
        z += 1
    print("z=", z)

    # Initialize variables
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q + 1)//2, p)

    print("M=", M)
    print("c=", c)
    print("t=", t)
    print("R=", R)

    while t != 1:
        print("LOOP")

        # Calculate i
        i = 0
        temp = t
        while temp != 1:
            i += 1
            temp = (temp * temp) % p
        print("i=", i)

        # Calculate b, M, c, t, R
        pow2 = 2 ** (M - i - 1)
        b = pow(c, pow2, p)
        M = i
        c = (b * b) % p
        t = (t * b * b) % p
        R = (R * b) % p
        print("b=", b)
        print("M=", M)
        print("c=", c)
        print("t=", t)
        print("R=", R)

    # We have found a square root
    return R

print("Square Root Tonelli Shanks: ",tonelli_shanks(p,a))
print(sqrt_mod(a, p)) # the same result

"""     CRT: Chinese Reminder Theorem
x ≡ a1 mod n1
x ≡ a2 mod n2
...
x ≡ an mod nn
=>There is a unique solution x ≡ a mod N where N = n1 * n2 * ... * nn
+ lezem n1,n2...nn coprime (premiers entre eux)

"""
"""
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17
"""
from sympy.ntheory.modular import crt
l=[2,3,5]
n=[5,11,17]
x=crt(n,l) #crt takhou en parametre liste des congru w lista des modulo + trajaa tuple fih l x wel modulo final
print("x=",x[0])
