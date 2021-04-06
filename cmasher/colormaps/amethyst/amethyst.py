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
cm_type = 'sequential'

# RGB-values of this colormap
cm_data = [[0.00000000, 0.00000000, 0.00000000],
           [0.00026424, 0.00021708, 0.00028431],
           [0.00092970, 0.00074511, 0.00101916],
           [0.00195182, 0.00152900, 0.00217634],
           [0.00331484, 0.00254258, 0.00375422],
           [0.00501100, 0.00376845, 0.00575809],
           [0.00703637, 0.00519353, 0.00819657],
           [0.00938920, 0.00680736, 0.01108027],
           [0.01206917, 0.00860113, 0.01442116],
           [0.01507694, 0.01056725, 0.01823225],
           [0.01841392, 0.01269897, 0.02252745],
           [0.02208207, 0.01499022, 0.02732142],
           [0.02608380, 0.01743543, 0.03262954],
           [0.03042188, 0.02002940, 0.03846783],
           [0.03509952, 0.02276720, 0.04464933],
           [0.04012007, 0.02564424, 0.05081384],
           [0.04523353, 0.02865615, 0.05697177],
           [0.05030216, 0.03179870, 0.06312822],
           [0.05533516, 0.03506780, 0.06928770],
           [0.06033640, 0.03845947, 0.07545419],
           [0.06530931, 0.04192822, 0.08163128],
           [0.07025691, 0.04533260, 0.08782221],
           [0.07518190, 0.04867984, 0.09402991],
           [0.08008669, 0.05197229, 0.10025709],
           [0.08497345, 0.05521205, 0.10650624],
           [0.08984468, 0.05840044, 0.11278112],
           [0.09470187, 0.06153938, 0.11908316],
           [0.09954649, 0.06463052, 0.12541389],
           [0.10438000, 0.06767518, 0.13177524],
           [0.10920379, 0.07067452, 0.13816903],
           [0.11401909, 0.07362957, 0.14459700],
           [0.11882787, 0.07654038, 0.15106315],
           [0.12363070, 0.07940829, 0.15756765],
           [0.12842832, 0.08223429, 0.16411134],
           [0.13322162, 0.08501902, 0.17069568],
           [0.13801182, 0.08776263, 0.17732315],
           [0.14280038, 0.09046479, 0.18399722],
           [0.14758705, 0.09312702, 0.19071635],
           [0.15237250, 0.09574970, 0.19748183],
           [0.15715826, 0.09833201, 0.20429774],
           [0.16194480, 0.10087429, 0.21116500],
           [0.16673190, 0.10337763, 0.21808261],
           [0.17152075, 0.10584130, 0.22505388],
           [0.17631241, 0.10826459, 0.23208194],
           [0.18110606, 0.11064913, 0.23916410],
           [0.18590324, 0.11299336, 0.24630520],
           [0.19070423, 0.11529734, 0.25350615],
           [0.19550828, 0.11756238, 0.26076476],
           [0.20031813, 0.11978497, 0.26809007],
           [0.20513167, 0.12196822, 0.27547552],
           [0.20995088, 0.12410941, 0.28292802],
           [0.21477508, 0.12620955, 0.29044580],
           [0.21960507, 0.12826738, 0.29803215],
           [0.22444084, 0.13028282, 0.30568765],
           [0.22928283, 0.13225497, 0.31341459],
           [0.23413080, 0.13418389, 0.32121301],
           [0.23898574, 0.13606767, 0.32908730],
           [0.24384625, 0.13790806, 0.33703369],
           [0.24871483, 0.13970049, 0.34506210],
           [0.25358923, 0.14144797, 0.35316594],
           [0.25847052, 0.14314802, 0.36135046],
           [0.26335917, 0.14479899, 0.36961891],
           [0.26825396, 0.14640203, 0.37796864],
           [0.27315531, 0.14795539, 0.38640302],
           [0.27806417, 0.14945618, 0.39492765],
           [0.28297910, 0.15090571, 0.40353941],
           [0.28790001, 0.15230275, 0.41224040],
           [0.29282677, 0.15364601, 0.42103271],
           [0.29775949, 0.15493361, 0.42991962],
           [0.30269797, 0.15616399, 0.43890356],
           [0.30764126, 0.15733701, 0.44798426],
           [0.31258891, 0.15845138, 0.45716364],
           [0.31754038, 0.15950581, 0.46644355],
           [0.32249501, 0.16049907, 0.47582575],
           [0.32745201, 0.16142998, 0.48531189],
           [0.33241046, 0.16229746, 0.49490348],
           [0.33736967, 0.16309963, 0.50460344],
           [0.34232881, 0.16383463, 0.51441474],
           [0.34728592, 0.16450300, 0.52433605],
           [0.35223936, 0.16510434, 0.53436800],
           [0.35718797, 0.16563665, 0.54451411],
           [0.36213040, 0.16609782, 0.55477822],
           [0.36706298, 0.16649188, 0.56515397],
           [0.37198552, 0.16681244, 0.57565304],
           [0.37689299, 0.16706658, 0.58626483],
           [0.38178435, 0.16724897, 0.59700002],
           [0.38665483, 0.16736482, 0.60785249],
           [0.39150048, 0.16741630, 0.61882203],
           [0.39631696, 0.16740583, 0.62990908],
           [0.40109916, 0.16733732, 0.64111292],
           [0.40584105, 0.16721663, 0.65243133],
           [0.41053556, 0.16705201, 0.66386021],
           [0.41517441, 0.16685477, 0.67539321],
           [0.41974795, 0.16663991, 0.68702119],
           [0.42424642, 0.16641935, 0.69874325],
           [0.42865593, 0.16622114, 0.71053811],
           [0.43296232, 0.16606992, 0.72239489],
           [0.43714833, 0.16600035, 0.73429359],
           [0.44119366, 0.16605689, 0.74620640],
           [0.44507497, 0.16629214, 0.75810111],
           [0.44876492, 0.16677496, 0.76992880],
           [0.45223283, 0.16757972, 0.78164083],
           [0.45544397, 0.16880100, 0.79316284],
           [0.45836096, 0.17054168, 0.80440956],
           [0.46094493, 0.17291044, 0.81528130],
           [0.46315959, 0.17601682, 0.82565706],
           [0.46497451, 0.17995217, 0.83541256],
           [0.46637118, 0.18477694, 0.84442326],
           [0.46734779, 0.19050472, 0.85258099],
           [0.46792136, 0.19709458, 0.85980957],
           [0.46812630, 0.20445531, 0.86607466],
           [0.46800986, 0.21246004, 0.87138503],
           [0.46762606, 0.22096576, 0.87578604],
           [0.46702908, 0.22983195, 0.87934856],
           [0.46626957, 0.23893263, 0.88215671],
           [0.46539292, 0.24816169, 0.88429869],
           [0.46443697, 0.25743572, 0.88585957],
           [0.46343365, 0.26669069, 0.88691806],
           [0.46240927, 0.27587938, 0.88754471],
           [0.46138628, 0.28496711, 0.88780241],
           [0.46038161, 0.29393135, 0.88774480],
           [0.45940980, 0.30275671, 0.88741881],
           [0.45848323, 0.31143335, 0.88686537],
           [0.45761161, 0.31995643, 0.88611932],
           [0.45680235, 0.32832487, 0.88520998],
           [0.45606325, 0.33653824, 0.88416454],
           [0.45539876, 0.34459984, 0.88300411],
           [0.45481491, 0.35251178, 0.88174987],
           [0.45431445, 0.36027928, 0.88041732],
           [0.45390085, 0.36790678, 0.87902148],
           [0.45357692, 0.37539912, 0.87757536],
           [0.45334512, 0.38276121, 0.87609062],
           [0.45320699, 0.38999847, 0.87457668],
           [0.45316394, 0.39711609, 0.87304215],
           [0.45321715, 0.40411911, 0.87149463],
           [0.45336773, 0.41101231, 0.86994117],
           [0.45361618, 0.41780059, 0.86838745],
           [0.45396291, 0.42448866, 0.86683856],
           [0.45440813, 0.43108098, 0.86529905],
           [0.45495195, 0.43758187, 0.86377294],
           [0.45559461, 0.44399517, 0.86226438],
           [0.45633578, 0.45032493, 0.86077628],
           [0.45717499, 0.45657506, 0.85931112],
           [0.45811209, 0.46274891, 0.85787191],
           [0.45914652, 0.46884993, 0.85646077],
           [0.46027749, 0.47488157, 0.85507921],
           [0.46150477, 0.48084655, 0.85372992],
           [0.46282717, 0.48674819, 0.85241350],
           [0.46424418, 0.49258908, 0.85113195],
           [0.46575477, 0.49837202, 0.84988609],
           [0.46735813, 0.50409951, 0.84867727],
           [0.46905322, 0.50977402, 0.84750623],
           [0.47083909, 0.51539785, 0.84637397],
           [0.47271463, 0.52097327, 0.84528104],
           [0.47467885, 0.52650233, 0.84422831],
           [0.47673053, 0.53198715, 0.84321604],
           [0.47886866, 0.53742955, 0.84224506],
           [0.48109197, 0.54283149, 0.84131544],
           [0.48339938, 0.54819466, 0.84042786],
           [0.48578964, 0.55352080, 0.83958239],
           [0.48826159, 0.55881150, 0.83877940],
           [0.49081400, 0.56406833, 0.83801910],
           [0.49344567, 0.56929278, 0.83730162],
           [0.49615539, 0.57448625, 0.83662720],
           [0.49894194, 0.57965013, 0.83599588],
           [0.50180411, 0.58478572, 0.83540778],
           [0.50474068, 0.58989428, 0.83486298],
           [0.50775048, 0.59497701, 0.83436152],
           [0.51083228, 0.60003510, 0.83390339],
           [0.51398493, 0.60506962, 0.83348870],
           [0.51720723, 0.61008170, 0.83311728],
           [0.52049804, 0.61507232, 0.83278930],
           [0.52385621, 0.62004252, 0.83250458],
           [0.52728061, 0.62499323, 0.83226318],
           [0.53077013, 0.62992537, 0.83206503],
           [0.53432367, 0.63483986, 0.83190999],
           [0.53794018, 0.63973753, 0.83179818],
           [0.54161857, 0.64461924, 0.83172925],
           [0.54535783, 0.64948575, 0.83170348],
           [0.54915693, 0.65433788, 0.83172038],
           [0.55301491, 0.65917633, 0.83178028],
           [0.55693076, 0.66400188, 0.83188269],
           [0.56090357, 0.66881516, 0.83202787],
           [0.56493240, 0.67361691, 0.83221545],
           [0.56901636, 0.67840775, 0.83244548],
           [0.57315458, 0.68318831, 0.83271789],
           [0.57734622, 0.68795924, 0.83303229],
           [0.58159045, 0.69272108, 0.83338902],
           [0.58588649, 0.69747446, 0.83378750],
           [0.59023358, 0.70221992, 0.83422784],
           [0.59463096, 0.70695796, 0.83471006],
           [0.59907795, 0.71168916, 0.83523370],
           [0.60357387, 0.71641401, 0.83579871],
           [0.60811806, 0.72113298, 0.83640513],
           [0.61270990, 0.72584655, 0.83705278],
           [0.61734884, 0.73055518, 0.83774138],
           [0.62203434, 0.73525935, 0.83847062],
           [0.62676587, 0.73995944, 0.83924056],
           [0.63154297, 0.74465587, 0.84005099],
           [0.63636521, 0.74934904, 0.84090170],
           [0.64123220, 0.75403932, 0.84179248],
           [0.64614362, 0.75872707, 0.84272311],
           [0.65109917, 0.76341264, 0.84369336],
           [0.65609861, 0.76809634, 0.84470300],
           [0.66114176, 0.77277847, 0.84575181],
           [0.66622856, 0.77745932, 0.84683929],
           [0.67135895, 0.78213915, 0.84796517],
           [0.67653291, 0.78681817, 0.84912944],
           [0.68175056, 0.79149658, 0.85033176],
           [0.68701224, 0.79617458, 0.85157118],
           [0.69231806, 0.80085226, 0.85284823],
           [0.69766865, 0.80552975, 0.85416159],
           [0.70306436, 0.81020708, 0.85551176],
           [0.70850604, 0.81488427, 0.85689766],
           [0.71399448, 0.81956126, 0.85831909],
           [0.71953066, 0.82423793, 0.85977578],
           [0.72511582, 0.82891409, 0.86126723],
           [0.73075140, 0.83358949, 0.86279302],
           [0.73643909, 0.83826376, 0.86435282],
           [0.74218079, 0.84293644, 0.86594641],
           [0.74797879, 0.84760693, 0.86757352],
           [0.75383582, 0.85227452, 0.86923372],
           [0.75975465, 0.85693832, 0.87092761],
           [0.76573885, 0.86159727, 0.87265510],
           [0.77179239, 0.86625009, 0.87441656],
           [0.77791962, 0.87089527, 0.87621315],
           [0.78412566, 0.87553101, 0.87804603],
           [0.79041634, 0.88015520, 0.87991695],
           [0.79679787, 0.88476539, 0.88182911],
           [0.80327764, 0.88935871, 0.88378592],
           [0.80986384, 0.89393178, 0.88579223],
           [0.81656525, 0.89848077, 0.88785493],
           [0.82339136, 0.90300133, 0.88998320],
           [0.83035266, 0.90748846, 0.89218842],
           [0.83745973, 0.91193666, 0.89448582],
           [0.84472274, 0.91634002, 0.89689514],
           [0.85215096, 0.92069239, 0.89944105],
           [0.85975062, 0.92498795, 0.90215463],
           [0.86752377, 0.92922171, 0.90507279],
           [0.87546482, 0.93339077, 0.90823842],
           [0.88355788, 0.93749566, 0.91169773],
           [0.89177570, 0.94154130, 0.91549519],
           [0.90007923, 0.94553793, 0.91966755],
           [0.90842150, 0.94950053, 0.92423680],
           [0.91675301, 0.95344729, 0.92920595],
           [0.92502858, 0.95739720, 0.93455848],
           [0.93321162, 0.96136803, 0.94026179],
           [0.94127596, 0.96537494, 0.94627265],
           [0.94920444, 0.96943048, 0.95254222],
           [0.95698652, 0.97354492, 0.95902011],
           [0.96461467, 0.97772735, 0.96565700],
           [0.97208078, 0.98198676, 0.97240707],
           [0.97937278, 0.98633302, 0.97923162],
           [0.98647225, 0.99077716, 0.98610463],
           [0.99335546, 0.99533023, 0.99302058],
           [1.00000000, 1.00000000, 1.00000000]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.amethyst', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
