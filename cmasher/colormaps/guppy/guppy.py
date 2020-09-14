# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = 'diverging'

# RGB-values of this colormap
cm_data = [[0.97913398, 0.56536368, 0.37127271],
           [0.97976590, 0.56105725, 0.36617941],
           [0.98039016, 0.55673301, 0.36108540],
           [0.98100660, 0.55239058, 0.35599072],
           [0.98161510, 0.54802956, 0.35089541],
           [0.98221551, 0.54364952, 0.34579953],
           [0.98280767, 0.53925004, 0.34070311],
           [0.98339143, 0.53483069, 0.33560621],
           [0.98396678, 0.53039090, 0.33050873],
           [0.98453372, 0.52593006, 0.32541055],
           [0.98509185, 0.52144789, 0.32031197],
           [0.98564100, 0.51694388, 0.31521307],
           [0.98618099, 0.51241753, 0.31011389],
           [0.98671214, 0.50786788, 0.30501398],
           [0.98723405, 0.50329458, 0.29991366],
           [0.98774629, 0.49869721, 0.29481320],
           [0.98824925, 0.49407472, 0.28971210],
           [0.98874258, 0.48942662, 0.28461059],
           [0.98922587, 0.48475242, 0.27950897],
           [0.98969970, 0.48005076, 0.27440646],
           [0.99016303, 0.47532167, 0.26930405],
           [0.99061673, 0.47056345, 0.26420065],
           [0.99105976, 0.46577606, 0.25909725],
           [0.99149262, 0.46095803, 0.25399314],
           [0.99191494, 0.45610865, 0.24888859],
           [0.99232636, 0.45122714, 0.24378385],
           [0.99272729, 0.44631195, 0.23867830],
           [0.99311732, 0.44136226, 0.23357226],
           [0.99349619, 0.43637703, 0.22846588],
           [0.99386383, 0.43135499, 0.22335910],
           [0.99422015, 0.42629483, 0.21825189],
           [0.99456504, 0.42119515, 0.21314426],
           [0.99489837, 0.41605450, 0.20803624],
           [0.99522002, 0.41087137, 0.20292790],
           [0.99552980, 0.40564418, 0.19781940],
           [0.99582752, 0.40037128, 0.19271090],
           [0.99611298, 0.39505092, 0.18760268],
           [0.99638591, 0.38968131, 0.18249509],
           [0.99664631, 0.38426022, 0.17738826],
           [0.99689415, 0.37878530, 0.17228241],
           [0.99712863, 0.37325500, 0.16717878],
           [0.99735036, 0.36766583, 0.16207703],
           [0.99755822, 0.36201632, 0.15697905],
           [0.99775273, 0.35630267, 0.15188492],
           [0.99793317, 0.35052253, 0.14679644],
           [0.99809921, 0.34467271, 0.14171519],
           [0.99825061, 0.33874971, 0.13664296],
           [0.99838704, 0.33274980, 0.13158209],
           [0.99850807, 0.32666908, 0.12653547],
           [0.99861318, 0.32050342, 0.12150677],
           [0.99870170, 0.31424850, 0.11650052],
           [0.99877311, 0.30789936, 0.11152205],
           [0.99882689, 0.30145048, 0.10657784],
           [0.99886191, 0.29489679, 0.10167648],
           [0.99887724, 0.28823232, 0.09682808],
           [0.99887207, 0.28145011, 0.09204481],
           [0.99884488, 0.27454372, 0.08734226],
           [0.99879434, 0.26750548, 0.08273916],
           [0.99871854, 0.26032782, 0.07825874],
           [0.99861505, 0.25300312, 0.07392952],
           [0.99848198, 0.24552156, 0.06978530],
           [0.99831584, 0.23787519, 0.06586779],
           [0.99811307, 0.23005492, 0.06222607],
           [0.99786925, 0.22205206, 0.05891766],
           [0.99757949, 0.21385746, 0.05600816],
           [0.99723702, 0.20546500, 0.05357050],
           [0.99683442, 0.19686899, 0.05168176],
           [0.99636255, 0.18806726, 0.05041901],
           [0.99581069, 0.17906196, 0.04985295],
           [0.99516626, 0.16986151, 0.05004038],
           [0.99441509, 0.16048211, 0.05101672],
           [0.99354131, 0.15095081, 0.05278951],
           [0.99252809, 0.14130676, 0.05533516],
           [0.99135888, 0.13160106, 0.05860026],
           [0.99001829, 0.12189766, 0.06250485],
           [0.98849390, 0.11226946, 0.06695080],
           [0.98677748, 0.10279463, 0.07183047],
           [0.98486585, 0.09355176, 0.07703595],
           [0.98276101, 0.08461546, 0.08246682],
           [0.98046964, 0.07605337, 0.08803598],
           [0.97800190, 0.06792645, 0.09367086],
           [0.97537034, 0.06028894, 0.09931552],
           [0.97258861, 0.05319146, 0.10492782],
           [0.96967062, 0.04668300, 0.11047736],
           [0.96662981, 0.04081237, 0.11594421],
           [0.96347883, 0.03571855, 0.12131510],
           [0.96022924, 0.03165348, 0.12658253],
           [0.95689153, 0.02851064, 0.13174239],
           [0.95347503, 0.02618830, 0.13679425],
           [0.94998813, 0.02459513, 0.14173838],
           [0.94643824, 0.02365009, 0.14657679],
           [0.94283185, 0.02328162, 0.15131275],
           [0.93917472, 0.02342641, 0.15594996],
           [0.93547208, 0.02402707, 0.16049112],
           [0.93172845, 0.02503369, 0.16494030],
           [0.92794785, 0.02640172, 0.16930129],
           [0.92413388, 0.02809128, 0.17357765],
           [0.92028982, 0.03006639, 0.17777258],
           [0.91641861, 0.03229466, 0.18188909],
           [0.91252265, 0.03474888, 0.18593131],
           [0.90860456, 0.03740117, 0.18990080],
           [0.90466625, 0.04022963, 0.19380129],
           [0.90070967, 0.04311436, 0.19763528],
           [0.89673660, 0.04600519, 0.20140502],
           [0.89274863, 0.04888784, 0.20511275],
           [0.88874720, 0.05174880, 0.20876066],
           [0.88473362, 0.05457784, 0.21235086],
           [0.88070903, 0.05736726, 0.21588543],
           [0.87667476, 0.06011007, 0.21936544],
           [0.87263168, 0.06280258, 0.22279306],
           [0.86858072, 0.06544162, 0.22616991],
           [0.86452287, 0.06802443, 0.22949710],
           [0.86045891, 0.07054964, 0.23277610],
           [0.85638946, 0.07301687, 0.23600864],
           [0.85231546, 0.07542467, 0.23919518],
           [0.84823749, 0.07777323, 0.24233709],
           [0.84415609, 0.08006302, 0.24543567],
           [0.84007187, 0.08229429, 0.24849184],
           [0.83598537, 0.08446754, 0.25150652],
           [0.83189711, 0.08658343, 0.25448057],
           [0.82780756, 0.08864274, 0.25741486],
           [0.82371716, 0.09064635, 0.26031021],
           [0.81962631, 0.09259520, 0.26316744],
           [0.81553541, 0.09449022, 0.26598725],
           [0.81144505, 0.09633167, 0.26876971],
           [0.80735534, 0.09812135, 0.27151621],
           [0.80326657, 0.09986032, 0.27422748],
           [0.79917933, 0.10154874, 0.27690333],
           [0.79509374, 0.10318811, 0.27954485],
           [0.79101004, 0.10477953, 0.28215273],
           [0.78692877, 0.10632317, 0.28472671],
           [0.78284983, 0.10782093, 0.28726828],
           [0.77877387, 0.10927265, 0.28977685],
           [0.77470081, 0.11068007, 0.29225373],
           [0.77063103, 0.11204357, 0.29469889],
           [0.76656481, 0.11336390, 0.29711264],
           [0.76250214, 0.11464238, 0.29949592],
           [0.75844350, 0.11587912, 0.30184841],
           [0.75438899, 0.11707510, 0.30417069],
           [0.75033870, 0.11823132, 0.30646340],
           [0.74629284, 0.11934839, 0.30872679],
           [0.74225176, 0.12042662, 0.31096074],
           [0.73821556, 0.12146683, 0.31316575],
           [0.73418433, 0.12246983, 0.31534230],
           [0.73015825, 0.12343620, 0.31749063],
           [0.72613750, 0.12436650, 0.31961098],
           [0.72212223, 0.12526128, 0.32170361],
           [0.71811261, 0.12612110, 0.32376876],
           [0.71410879, 0.12694648, 0.32580667],
           [0.71011091, 0.12773792, 0.32781758],
           [0.70611911, 0.12849593, 0.32980172],
           [0.70213354, 0.12922099, 0.33175934],
           [0.69815432, 0.12991357, 0.33369067],
           [0.69418157, 0.13057411, 0.33559594],
           [0.69021544, 0.13120307, 0.33747540],
           [0.68625603, 0.13180086, 0.33932927],
           [0.68230346, 0.13236790, 0.34115779],
           [0.67835786, 0.13290458, 0.34296119],
           [0.67441945, 0.13341107, 0.34473941],
           [0.67048833, 0.13388775, 0.34649271],
           [0.66656453, 0.13433515, 0.34822154],
           [0.66264814, 0.13475362, 0.34992614],
           [0.65873927, 0.13514347, 0.35160674],
           [0.65483833, 0.13550453, 0.35326289],
           [0.65094515, 0.13583755, 0.35489542],
           [0.64705980, 0.13614285, 0.35650463],
           [0.64318255, 0.13642043, 0.35809038],
           [0.63931356, 0.13667048, 0.35965276],
           [0.63545272, 0.13689358, 0.36119251],
           [0.63160031, 0.13708967, 0.36270943],
           [0.62775649, 0.13725891, 0.36420366],
           [0.62392110, 0.13740188, 0.36567597],
           [0.62009464, 0.13751818, 0.36712575],
           [0.61627690, 0.13760846, 0.36855391],
           [0.61246810, 0.13767272, 0.36996045],
           [0.60866843, 0.13771098, 0.37134540],
           [0.60487778, 0.13772371, 0.37270949],
           [0.60109660, 0.13771054, 0.37405221],
           [0.59732458, 0.13767217, 0.37537471],
           [0.59356230, 0.13760803, 0.37667623],
           [0.58980937, 0.13751892, 0.37795807],
           [0.58606640, 0.13740422, 0.37921945],
           [0.58233303, 0.13726463, 0.38046161],
           [0.57860976, 0.13709969, 0.38168400],
           [0.57489642, 0.13690981, 0.38288750],
           [0.57119325, 0.13669482, 0.38407208],
           [0.56750038, 0.13645474, 0.38523804],
           [0.56381771, 0.13618982, 0.38638606],
           [0.56014575, 0.13589956, 0.38751565],
           [0.55648419, 0.13558446, 0.38862799],
           [0.55283337, 0.13524418, 0.38972291],
           [0.54919340, 0.13487871, 0.39080076],
           [0.54556418, 0.13448819, 0.39186229],
           [0.54194611, 0.13407223, 0.39290725],
           [0.53833913, 0.13363092, 0.39393635],
           [0.53474326, 0.13316427, 0.39495016],
           [0.53115882, 0.13267190, 0.39594857],
           [0.52758584, 0.13215378, 0.39693220],
           [0.52402429, 0.13160989, 0.39790168],
           [0.52047436, 0.13103997, 0.39885725],
           [0.51693633, 0.13044365, 0.39979899],
           [0.51341006, 0.12982098, 0.40072783],
           [0.50989568, 0.12917172, 0.40164420],
           [0.50639337, 0.12849553, 0.40254833],
           [0.50290332, 0.12779205, 0.40344056],
           [0.49942546, 0.12706118, 0.40432170],
           [0.49595991, 0.12630258, 0.40519224],
           [0.49250676, 0.12551592, 0.40605268],
           [0.48906629, 0.12470066, 0.40690317],
           [0.48563847, 0.12385654, 0.40774452],
           [0.48222337, 0.12298317, 0.40857735],
           [0.47882107, 0.12208010, 0.40940222],
           [0.47543168, 0.12114683, 0.41021970],
           [0.47205532, 0.12018283, 0.41103034],
           [0.46869220, 0.11918741, 0.41183445],
           [0.46534229, 0.11816010, 0.41263296],
           [0.46200568, 0.11710026, 0.41342649],
           [0.45868247, 0.11600718, 0.41421569],
           [0.45537275, 0.11488011, 0.41500120],
           [0.45207661, 0.11371825, 0.41578368],
           [0.44879417, 0.11252073, 0.41656383],
           [0.44552551, 0.11128661, 0.41734234],
           [0.44227075, 0.11001487, 0.41811986],
           [0.43903002, 0.10870441, 0.41889708],
           [0.43580336, 0.10735411, 0.41967485],
           [0.43259086, 0.10596269, 0.42045394],
           [0.42939262, 0.10452878, 0.42123513],
           [0.42620875, 0.10305091, 0.42201921],
           [0.42303935, 0.10152745, 0.42280698],
           [0.41988452, 0.09995666, 0.42359927],
           [0.41674438, 0.09833662, 0.42439693],
           [0.41361903, 0.09666524, 0.42520082],
           [0.41050859, 0.09494025, 0.42601181],
           [0.40741317, 0.09315912, 0.42683080],
           [0.40433289, 0.09131911, 0.42765870],
           [0.40126789, 0.08941717, 0.42849646],
           [0.39821830, 0.08744994, 0.42934503],
           [0.39518425, 0.08541368, 0.43020538],
           [0.39216589, 0.08330422, 0.43107852],
           [0.38916338, 0.08111690, 0.43196545],
           [0.38617687, 0.07884649, 0.43286722],
           [0.38320653, 0.07648706, 0.43378489],
           [0.38025255, 0.07403192, 0.43471956],
           [0.37731512, 0.07147337, 0.43567234],
           [0.37439443, 0.06880262, 0.43664437],
           [0.37149072, 0.06600943, 0.43763682],
           [0.36860424, 0.06308188, 0.43865075],
           [0.36573522, 0.06000590, 0.43968746],
           [0.36288391, 0.05676472, 0.44074825],
           [0.36005059, 0.05333809, 0.44183442],
           [0.35723556, 0.04970120, 0.44294730],
           [0.35443913, 0.04582314, 0.44408825],
           [0.35166165, 0.04166457, 0.44525868],
           [0.34890349, 0.03719795, 0.44646003],
           [0.34616504, 0.03263529, 0.44769379],
           [0.34344673, 0.02800691, 0.44896150],
           [0.34479501, 0.03011083, 0.45429784],
           [0.34613298, 0.03223021, 0.45965587],
           [0.34746048, 0.03436478, 0.46503586],
           [0.34877738, 0.03651433, 0.47043804],
           [0.35008349, 0.03867868, 0.47586266],
           [0.35137865, 0.04084965, 0.48130991],
           [0.35266266, 0.04296120, 0.48677998],
           [0.35393531, 0.04502423, 0.49227313],
           [0.35519633, 0.04704222, 0.49778979],
           [0.35644553, 0.04901862, 0.50332975],
           [0.35768269, 0.05095638, 0.50889311],
           [0.35890752, 0.05285819, 0.51447999],
           [0.36011967, 0.05472629, 0.52009100],
           [0.36131893, 0.05656330, 0.52572559],
           [0.36250500, 0.05837140, 0.53138377],
           [0.36367743, 0.06015228, 0.53706623],
           [0.36483600, 0.06190822, 0.54277228],
           [0.36598032, 0.06364099, 0.54850200],
           [0.36710993, 0.06535216, 0.55425570],
           [0.36822457, 0.06704382, 0.56003256],
           [0.36932365, 0.06871713, 0.56583342],
           [0.37040690, 0.07037425, 0.57165704],
           [0.37147370, 0.07201627, 0.57750421],
           [0.37252373, 0.07364527, 0.58337370],
           [0.37355632, 0.07526233, 0.58926620],
           [0.37457109, 0.07686942, 0.59518056],
           [0.37556742, 0.07846791, 0.60111680],
           [0.37654472, 0.08005935, 0.60707458],
           [0.37750246, 0.08164553, 0.61305301],
           [0.37843994, 0.08322788, 0.61905195],
           [0.37935652, 0.08480803, 0.62507086],
           [0.38025156, 0.08638779, 0.63110879],
           [0.38112434, 0.08796885, 0.63716509],
           [0.38197410, 0.08955290, 0.64323912],
           [0.38280001, 0.09114162, 0.64933029],
           [0.38360134, 0.09273698, 0.65543740],
           [0.38437722, 0.09434085, 0.66155950],
           [0.38512678, 0.09595517, 0.66769558],
           [0.38584910, 0.09758190, 0.67384452],
           [0.38654322, 0.09922310, 0.68000511],
           [0.38720815, 0.10088086, 0.68617606],
           [0.38784284, 0.10255736, 0.69235596],
           [0.38844622, 0.10425482, 0.69854331],
           [0.38901718, 0.10597554, 0.70473649],
           [0.38955446, 0.10772176, 0.71093406],
           [0.39005689, 0.10949595, 0.71713406],
           [0.39052322, 0.11130063, 0.72333440],
           [0.39095216, 0.11313837, 0.72953294],
           [0.39134220, 0.11501156, 0.73572799],
           [0.39169199, 0.11692297, 0.74191684],
           [0.39200011, 0.11887536, 0.74809688],
           [0.39226481, 0.12087123, 0.75426612],
           [0.39248473, 0.12291363, 0.76042095],
           [0.39265793, 0.12500509, 0.76655935],
           [0.39278294, 0.12714868, 0.77267742],
           [0.39285780, 0.12934713, 0.77877236],
           [0.39288070, 0.13160332, 0.78484064],
           [0.39284978, 0.13392017, 0.79087839],
           [0.39276304, 0.13630052, 0.79688191],
           [0.39261831, 0.13874713, 0.80284745],
           [0.39241363, 0.14126288, 0.80877047],
           [0.39214683, 0.14385050, 0.81464656],
           [0.39181569, 0.14651269, 0.82047110],
           [0.39141795, 0.14925205, 0.82623923],
           [0.39095130, 0.15207108, 0.83194590],
           [0.39041340, 0.15497218, 0.83758579],
           [0.38980189, 0.15795759, 0.84315342],
           [0.38911433, 0.16102942, 0.84864316],
           [0.38834823, 0.16418957, 0.85404921],
           [0.38750132, 0.16743977, 0.85936527],
           [0.38657121, 0.17078150, 0.86458509],
           [0.38555525, 0.17421602, 0.86970262],
           [0.38445141, 0.17774426, 0.87471089],
           [0.38325716, 0.18136695, 0.87960359],
           [0.38197051, 0.18508438, 0.88437372],
           [0.38058910, 0.18889664, 0.88901480],
           [0.37911118, 0.19280333, 0.89351978],
           [0.37753482, 0.19680375, 0.89788204],
           [0.37585829, 0.20089681, 0.90209496],
           [0.37408024, 0.20508093, 0.90615190],
           [0.37219944, 0.20935418, 0.91004655],
           [0.37021490, 0.21371418, 0.91377282],
           [0.36812590, 0.21815814, 0.91732493],
           [0.36593203, 0.22268286, 0.92069747],
           [0.36363331, 0.22728466, 0.92388544],
           [0.36123002, 0.23195951, 0.92688435],
           [0.35872282, 0.23670299, 0.92969027],
           [0.35611277, 0.24151035, 0.93229987],
           [0.35340128, 0.24637649, 0.93471048],
           [0.35059019, 0.25129607, 0.93692014],
           [0.34768169, 0.25626348, 0.93892761],
           [0.34467838, 0.26127295, 0.94073239],
           [0.34158321, 0.26631857, 0.94233477],
           [0.33839949, 0.27139435, 0.94373579],
           [0.33513081, 0.27649425, 0.94493725],
           [0.33178111, 0.28161230, 0.94594169],
           [0.32835454, 0.28674257, 0.94675233],
           [0.32485551, 0.29187927, 0.94737307],
           [0.32128860, 0.29701680, 0.94780841],
           [0.31765858, 0.30214973, 0.94806342],
           [0.31397030, 0.30727291, 0.94814364],
           [0.31022870, 0.31238146, 0.94805506],
           [0.30643878, 0.31747080, 0.94780400],
           [0.30260563, 0.32253663, 0.94739714],
           [0.29873427, 0.32757500, 0.94684135],
           [0.29482957, 0.33258236, 0.94614364],
           [0.29089641, 0.33755548, 0.94531111],
           [0.28693973, 0.34249136, 0.94435103],
           [0.28296437, 0.34738736, 0.94327063],
           [0.27897461, 0.35224137, 0.94207688],
           [0.27497549, 0.35705118, 0.94077712],
           [0.27097085, 0.36181536, 0.93937798],
           [0.26696552, 0.36653225, 0.93788660],
           [0.26296308, 0.37120096, 0.93630923],
           [0.25896806, 0.37582036, 0.93465261],
           [0.25498411, 0.38038987, 0.93292280],
           [0.25101488, 0.38490906, 0.93112571],
           [0.24706409, 0.38937762, 0.92926711],
           [0.24313548, 0.39379533, 0.92735264],
           [0.23923241, 0.39816227, 0.92538753],
           [0.23535811, 0.40247866, 0.92337670],
           [0.23151584, 0.40674478, 0.92132494],
           [0.22770873, 0.41096104, 0.91923677],
           [0.22393985, 0.41512795, 0.91711647],
           [0.22021254, 0.41924599, 0.91496834],
           [0.21652943, 0.42331591, 0.91279602],
           [0.21289334, 0.42733848, 0.91060306],
           [0.20930700, 0.43131450, 0.90839281],
           [0.20577373, 0.43524461, 0.90616889],
           [0.20229584, 0.43912982, 0.90393399],
           [0.19887588, 0.44297107, 0.90169084],
           [0.19551717, 0.44676907, 0.89944259],
           [0.19222147, 0.45052503, 0.89719109],
           [0.18899228, 0.45423962, 0.89493934],
           [0.18583140, 0.45791403, 0.89268896],
           [0.18274164, 0.46154916, 0.89044220],
           [0.17972576, 0.46514588, 0.88820117],
           [0.17678569, 0.46870532, 0.88596725],
           [0.17392390, 0.47222843, 0.88374214],
           [0.17114328, 0.47571601, 0.88152782],
           [0.16844568, 0.47916915, 0.87932535],
           [0.16583329, 0.48258880, 0.87713604],
           [0.16330828, 0.48597588, 0.87496114],
           [0.16087272, 0.48933132, 0.87280181],
           [0.15852859, 0.49265603, 0.87065910],
           [0.15627773, 0.49595091, 0.86853398],
           [0.15412185, 0.49921683, 0.86642734],
           [0.15206252, 0.50245468, 0.86433997],
           [0.15010115, 0.50566533, 0.86227263],
           [0.14823898, 0.50884960, 0.86022596],
           [0.14647705, 0.51200835, 0.85820057],
           [0.14481633, 0.51514235, 0.85619707],
           [0.14325781, 0.51825234, 0.85421625],
           [0.14180153, 0.52133918, 0.85225819],
           [0.14044768, 0.52440367, 0.85032327],
           [0.13919648, 0.52744649, 0.84841203],
           [0.13804793, 0.53046832, 0.84652501],
           [0.13700099, 0.53347000, 0.84466201],
           [0.13605533, 0.53645214, 0.84282363],
           [0.13520996, 0.53941544, 0.84101007],
           [0.13446323, 0.54236064, 0.83922115],
           [0.13381443, 0.54528824, 0.83745772],
           [0.13326089, 0.54819910, 0.83571901],
           [0.13280172, 0.55109359, 0.83400610],
           [0.13243371, 0.55397257, 0.83231809],
           [0.13215537, 0.55683644, 0.83065585],
           [0.13196346, 0.55968594, 0.82901876],
           [0.13185556, 0.56252157, 0.82740713],
           [0.13182883, 0.56534387, 0.82582099],
           [0.13187981, 0.56815348, 0.82425992],
           [0.13200583, 0.57095084, 0.82272434],
           [0.13220335, 0.57373651, 0.82121393],
           [0.13246881, 0.57651105, 0.81972840],
           [0.13279896, 0.57927494, 0.81826783],
           [0.13319049, 0.58202860, 0.81683230],
           [0.13363949, 0.58477261, 0.81542130],
           [0.13414244, 0.58750743, 0.81403468],
           [0.13469577, 0.59023352, 0.81267228],
           [0.13529611, 0.59295129, 0.81133415],
           [0.13593981, 0.59566121, 0.81001996],
           [0.13662322, 0.59836372, 0.80872939],
           [0.13734287, 0.60105927, 0.80746220],
           [0.13809532, 0.60374827, 0.80621816],
           [0.13887717, 0.60643112, 0.80499702],
           [0.13968511, 0.60910822, 0.80379851],
           [0.14051586, 0.61177998, 0.80262236],
           [0.14136623, 0.61444677, 0.80146827],
           [0.14223308, 0.61710899, 0.80033595],
           [0.14311336, 0.61976699, 0.79922506],
           [0.14400410, 0.62242115, 0.79813528],
           [0.14490239, 0.62507183, 0.79706628],
           [0.14580541, 0.62771937, 0.79601771],
           [0.14671039, 0.63036413, 0.79498919],
           [0.14761466, 0.63300644, 0.79398037],
           [0.14851562, 0.63564664, 0.79299085],
           [0.14941074, 0.63828506, 0.79202024],
           [0.15029754, 0.64092201, 0.79106814],
           [0.15117363, 0.64355782, 0.79013413],
           [0.15203691, 0.64619274, 0.78921804],
           [0.15288495, 0.64882711, 0.78831926],
           [0.15371549, 0.65146123, 0.78743730],
           [0.15452637, 0.65409541, 0.78657171],
           [0.15531547, 0.65672993, 0.78572203],
           [0.15608099, 0.65936502, 0.78488802],
           [0.15682087, 0.66200097, 0.78406918],
           [0.15753297, 0.66463807, 0.78326482],
           [0.15821536, 0.66727660, 0.78247447],
           [0.15886645, 0.66991676, 0.78169791],
           [0.15948431, 0.67255881, 0.78093456],
           [0.16006689, 0.67520305, 0.78018370],
           [0.16061251, 0.67784968, 0.77944492],
           [0.16111977, 0.68049889, 0.77871803],
           [0.16158641, 0.68315100, 0.77800205],
           [0.16201082, 0.68580619, 0.77729656],
           [0.16239169, 0.68846463, 0.77660137],
           [0.16272671, 0.69112662, 0.77591543],
           [0.16301457, 0.69379231, 0.77523853],
           [0.16325354, 0.69646191, 0.77457010],
           [0.16344146, 0.69913567, 0.77390921],
           [0.16357752, 0.70181366, 0.77325602],
           [0.16365904, 0.70449619, 0.77260922],
           [0.16368488, 0.70718337, 0.77196871],
           [0.16365298, 0.70987540, 0.77133368],
           [0.16356156, 0.71257245, 0.77070358],
           [0.16340899, 0.71527466, 0.77007797],
           [0.16319301, 0.71798224, 0.76945599],
           [0.16291224, 0.72069528, 0.76883739],
           [0.16256408, 0.72341399, 0.76822119],
           [0.16214715, 0.72613844, 0.76760720],
           [0.16165868, 0.72886886, 0.76699440],
           [0.16109710, 0.73160529, 0.76638256],
           [0.16045965, 0.73434793, 0.76577079],
           [0.15974424, 0.73709686, 0.76515863],
           [0.15894834, 0.73985220, 0.76454547],
           [0.15806904, 0.74261410, 0.76393052],
           [0.15710427, 0.74538258, 0.76331354],
           [0.15605009, 0.74815788, 0.76269339],
           [0.15490465, 0.75093993, 0.76207009],
           [0.15366358, 0.75372895, 0.76144248],
           [0.15232374, 0.75652499, 0.76081016],
           [0.15088169, 0.75932808, 0.76017268],
           [0.14933248, 0.76213840, 0.75952902],
           [0.14767273, 0.76495591, 0.75887905],
           [0.14589703, 0.76778075, 0.75822189],
           [0.14399973, 0.77061300, 0.75755675],
           [0.14197646, 0.77345261, 0.75688361],
           [0.13981974, 0.77629973, 0.75620137],
           [0.13752244, 0.77915443, 0.75550938],
           [0.13507816, 0.78201663, 0.75480758],
           [0.13247713, 0.78488648, 0.75409493],
           [0.12970941, 0.78776402, 0.75337079],
           [0.12676492, 0.79064921, 0.75263491],
           [0.12363087, 0.79354209, 0.75188660],
           [0.12029222, 0.79644276, 0.75112509],
           [0.11673226, 0.79935121, 0.75034980]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.guppy', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
