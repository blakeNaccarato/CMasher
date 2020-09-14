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
           [0.00023591, 0.00015584, 0.00012983],
           [0.00084268, 0.00053302, 0.00043311],
           [0.00179367, 0.00108986, 0.00086448],
           [0.00308329, 0.00180640, 0.00140039],
           [0.00471108, 0.00266932, 0.00202446],
           [0.00667873, 0.00366872, 0.00272405],
           [0.00898911, 0.00479674, 0.00348880],
           [0.01164575, 0.00604687, 0.00430991],
           [0.01465261, 0.00741359, 0.00517969],
           [0.01801393, 0.00889211, 0.00609130],
           [0.02173412, 0.01047822, 0.00703857],
           [0.02581773, 0.01216815, 0.00801582],
           [0.03026940, 0.01395853, 0.00901785],
           [0.03509381, 0.01584628, 0.01003979],
           [0.04029567, 0.01782862, 0.01107709],
           [0.04559319, 0.01990296, 0.01212542],
           [0.05085458, 0.02206679, 0.01318043],
           [0.05608526, 0.02431808, 0.01423851],
           [0.06128816, 0.02665483, 0.01529599],
           [0.06646583, 0.02907520, 0.01634937],
           [0.07162119, 0.03157716, 0.01739463],
           [0.07675565, 0.03415935, 0.01842896],
           [0.08187073, 0.03682041, 0.01944937],
           [0.08696885, 0.03955851, 0.02045189],
           [0.09205052, 0.04231495, 0.02143435],
           [0.09711732, 0.04502661, 0.02239342],
           [0.10217028, 0.04770463, 0.02332627],
           [0.10721024, 0.05035078, 0.02423019],
           [0.11223800, 0.05296671, 0.02510249],
           [0.11725454, 0.05555381, 0.02594016],
           [0.12225988, 0.05811389, 0.02674134],
           [0.12725523, 0.06064795, 0.02750256],
           [0.13224067, 0.06315756, 0.02822177],
           [0.13721639, 0.06564411, 0.02889673],
           [0.14218274, 0.06810886, 0.02952495],
           [0.14713996, 0.07055301, 0.03010397],
           [0.15208833, 0.07297770, 0.03063115],
           [0.15702766, 0.07538431, 0.03110457],
           [0.16195785, 0.07777409, 0.03152207],
           [0.16687891, 0.08014820, 0.03188116],
           [0.17179059, 0.08250792, 0.03217971],
           [0.17669241, 0.08485465, 0.03241590],
           [0.18158383, 0.08718981, 0.03258789],
           [0.18646448, 0.08951466, 0.03269335],
           [0.19133390, 0.09183056, 0.03272990],
           [0.19619078, 0.09413935, 0.03269677],
           [0.20103478, 0.09644230, 0.03259085],
           [0.20586442, 0.09874137, 0.03241120],
           [0.21067840, 0.10103843, 0.03215627],
           [0.21547534, 0.10333543, 0.03182425],
           [0.22025361, 0.10563450, 0.03141354],
           [0.22501120, 0.10793803, 0.03092289],
           [0.22974575, 0.11024868, 0.03035144],
           [0.23445444, 0.11256943, 0.02969879],
           [0.23913453, 0.11490331, 0.02896358],
           [0.24378211, 0.11725411, 0.02814675],
           [0.24839355, 0.11962551, 0.02724723],
           [0.25296377, 0.12202222, 0.02626713],
           [0.25748730, 0.12444922, 0.02520817],
           [0.26195802, 0.12691203, 0.02407252],
           [0.26636848, 0.12941702, 0.02286492],
           [0.27071043, 0.13197113, 0.02159076],
           [0.27497435, 0.13458210, 0.02025819],
           [0.27914966, 0.13725827, 0.01887748],
           [0.28322473, 0.14000849, 0.01746200],
           [0.28718711, 0.14284181, 0.01602831],
           [0.29102397, 0.14576709, 0.01459717],
           [0.29472285, 0.14879225, 0.01319285],
           [0.29827261, 0.15192362, 0.01184251],
           [0.30166442, 0.15516506, 0.01057506],
           [0.30489281, 0.15851736, 0.00942006],
           [0.30795616, 0.16197801, 0.00840479],
           [0.31085688, 0.16554138, 0.00755322],
           [0.31360089, 0.16919930, 0.00688466],
           [0.31619667, 0.17294207, 0.00641320],
           [0.31865438, 0.17675921, 0.00614872],
           [0.32098465, 0.18064045, 0.00609697],
           [0.32319802, 0.18457612, 0.00626128],
           [0.32530438, 0.18855752, 0.00664327],
           [0.32731268, 0.19257708, 0.00724361],
           [0.32923105, 0.19662814, 0.00806290],
           [0.33106622, 0.20070536, 0.00910151],
           [0.33282455, 0.20480389, 0.01036052],
           [0.33451106, 0.20892003, 0.01184121],
           [0.33613028, 0.21305052, 0.01354550],
           [0.33768610, 0.21719270, 0.01547588],
           [0.33918193, 0.22134430, 0.01763530],
           [0.34062084, 0.22550339, 0.02002721],
           [0.34200502, 0.22966865, 0.02265548],
           [0.34333725, 0.23383843, 0.02552433],
           [0.34461908, 0.23801193, 0.02863839],
           [0.34585240, 0.24218815, 0.03200252],
           [0.34703896, 0.24636622, 0.03562179],
           [0.34818014, 0.25054550, 0.03950152],
           [0.34927719, 0.25472546, 0.04352393],
           [0.35033133, 0.25890562, 0.04756206],
           [0.35134375, 0.26308551, 0.05162286],
           [0.35231551, 0.26726476, 0.05570435],
           [0.35324745, 0.27144313, 0.05980501],
           [0.35414045, 0.27562036, 0.06392355],
           [0.35499557, 0.27979613, 0.06805876],
           [0.35581354, 0.28397028, 0.07220974],
           [0.35659502, 0.28814269, 0.07637572],
           [0.35734105, 0.29231309, 0.08055578],
           [0.35805201, 0.29648150, 0.08474942],
           [0.35872891, 0.30064767, 0.08895578],
           [0.35937222, 0.30481162, 0.09317434],
           [0.35998258, 0.30897327, 0.09740444],
           [0.36056084, 0.31313246, 0.10164532],
           [0.36110736, 0.31728928, 0.10589648],
           [0.36162275, 0.32144368, 0.11015721],
           [0.36210777, 0.32559556, 0.11442673],
           [0.36256280, 0.32974502, 0.11870441],
           [0.36298834, 0.33389206, 0.12298953],
           [0.36338488, 0.33803673, 0.12728134],
           [0.36375290, 0.34217907, 0.13157904],
           [0.36409290, 0.34631911, 0.13588179],
           [0.36440520, 0.35045697, 0.14018879],
           [0.36469016, 0.35459276, 0.14449920],
           [0.36494810, 0.35872659, 0.14881214],
           [0.36517929, 0.36285859, 0.15312671],
           [0.36538396, 0.36698891, 0.15744199],
           [0.36556231, 0.37111773, 0.16175705],
           [0.36571447, 0.37524523, 0.16607092],
           [0.36584051, 0.37937162, 0.17038263],
           [0.36594045, 0.38349712, 0.17469120],
           [0.36601425, 0.38762197, 0.17899563],
           [0.36606181, 0.39174644, 0.18329490],
           [0.36608293, 0.39587081, 0.18758800],
           [0.36607737, 0.39999537, 0.19187390],
           [0.36604481, 0.40412044, 0.19615155],
           [0.36598484, 0.40824635, 0.20041993],
           [0.36589697, 0.41237347, 0.20467797],
           [0.36578063, 0.41650216, 0.20892463],
           [0.36563516, 0.42063281, 0.21315884],
           [0.36545982, 0.42476582, 0.21737953],
           [0.36525376, 0.42890161, 0.22158565],
           [0.36501603, 0.43304063, 0.22577610],
           [0.36474562, 0.43718331, 0.22994981],
           [0.36444137, 0.44133014, 0.23410567],
           [0.36410206, 0.44548157, 0.23824257],
           [0.36372631, 0.44963813, 0.24235941],
           [0.36331269, 0.45380030, 0.24645504],
           [0.36285964, 0.45796860, 0.25052829],
           [0.36236549, 0.46214356, 0.25457799],
           [0.36182846, 0.46632571, 0.25860290],
           [0.36124664, 0.47051561, 0.26260178],
           [0.36061804, 0.47471380, 0.26657334],
           [0.35994053, 0.47892085, 0.27051623],
           [0.35921186, 0.48313732, 0.27442906],
           [0.35842966, 0.48736379, 0.27831038],
           [0.35759129, 0.49160087, 0.28215871],
           [0.35669425, 0.49584911, 0.28597239],
           [0.35573584, 0.50010908, 0.28974975],
           [0.35471320, 0.50438137, 0.29348899],
           [0.35362322, 0.50866660, 0.29718825],
           [0.35246273, 0.51296535, 0.30084552],
           [0.35122869, 0.51727815, 0.30445862],
           [0.34991767, 0.52160560, 0.30802530],
           [0.34852593, 0.52594832, 0.31154314],
           [0.34705031, 0.53030675, 0.31500949],
           [0.34548671, 0.53468153, 0.31842163],
           [0.34383161, 0.53907312, 0.32177654],
           [0.34208104, 0.54348204, 0.32507106],
           [0.34023110, 0.54790874, 0.32830182],
           [0.33827779, 0.55235367, 0.33146519],
           [0.33621736, 0.55681717, 0.33455732],
           [0.33404546, 0.56129968, 0.33757415],
           [0.33175876, 0.56580136, 0.34051135],
           [0.32935326, 0.57032249, 0.34336436],
           [0.32682534, 0.57486322, 0.34612840],
           [0.32417204, 0.57942352, 0.34879848],
           [0.32139041, 0.58400334, 0.35136941],
           [0.31847786, 0.58860252, 0.35383585],
           [0.31543240, 0.59322076, 0.35619234],
           [0.31225296, 0.59785756, 0.35843338],
           [0.30893902, 0.60251232, 0.36055346],
           [0.30549095, 0.60718426, 0.36254717],
           [0.30191012, 0.61187244, 0.36440927],
           [0.29819897, 0.61657573, 0.36613479],
           [0.29436110, 0.62129287, 0.36771914],
           [0.29040133, 0.62602242, 0.36915820],
           [0.28632570, 0.63076280, 0.37044843],
           [0.28214143, 0.63551231, 0.37158696],
           [0.27785706, 0.64026917, 0.37257168],
           [0.27348193, 0.64503154, 0.37340120],
           [0.26902633, 0.64979759, 0.37407498],
           [0.26450121, 0.65456550, 0.37459320],
           [0.25991797, 0.65933353, 0.37495680],
           [0.25528911, 0.66409992, 0.37516769],
           [0.25062654, 0.66886315, 0.37522811],
           [0.24594117, 0.67362199, 0.37514051],
           [0.24124719, 0.67837487, 0.37490901],
           [0.23655318, 0.68312112, 0.37453605],
           [0.23187328, 0.68785948, 0.37402657],
           [0.22721600, 0.69258952, 0.37338359],
           [0.22259162, 0.69731068, 0.37261100],
           [0.21801018, 0.70202253, 0.37171275],
           [0.21348139, 0.70672478, 0.37069276],
           [0.20901357, 0.71141737, 0.36955433],
           [0.20461573, 0.71610024, 0.36830104],
           [0.20029548, 0.72077353, 0.36693570],
           [0.19606012, 0.72543750, 0.36546082],
           [0.19191644, 0.73009247, 0.36387842],
           [0.18787403, 0.73473853, 0.36219178],
           [0.18393926, 0.73937614, 0.36040226],
           [0.18011896, 0.74400575, 0.35851116],
           [0.17642112, 0.74862770, 0.35652009],
           [0.17285420, 0.75324234, 0.35443069],
           [0.16942317, 0.75785034, 0.35224224],
           [0.16613636, 0.76245208, 0.34995563],
           [0.16300457, 0.76704773, 0.34757300],
           [0.16003262, 0.77163802, 0.34509256],
           [0.15722844, 0.77622337, 0.34251413],
           [0.15459987, 0.78080421, 0.33983723],
           [0.15215452, 0.78538097, 0.33706103],
           [0.14989970, 0.78995411, 0.33418434],
           [0.14784393, 0.79452393, 0.33120673],
           [0.14599455, 0.79909080, 0.32812698],
           [0.14435597, 0.80365529, 0.32494176],
           [0.14293350, 0.80821783, 0.32164835],
           [0.14173566, 0.81277853, 0.31824683],
           [0.14076563, 0.81733786, 0.31473343],
           [0.14002424, 0.82189641, 0.31110254],
           [0.13952106, 0.82645397, 0.30735665],
           [0.13924955, 0.83101154, 0.30348438],
           [0.13921938, 0.83556872, 0.29948985],
           [0.13942231, 0.84012646, 0.29536052],
           [0.13986269, 0.84468460, 0.29109694],
           [0.14053561, 0.84924364, 0.28669062],
           [0.14143644, 0.85380396, 0.28213343],
           [0.14256553, 0.85836545, 0.27742378],
           [0.14391460, 0.86292863, 0.27254985],
           [0.14547751, 0.86749380, 0.26750209],
           [0.14724827, 0.87206117, 0.26227091],
           [0.14922184, 0.87663078, 0.25684817],
           [0.15138996, 0.88120296, 0.25121997],
           [0.15374428, 0.88577799, 0.24537071],
           [0.15627712, 0.89035608, 0.23928425],
           [0.15898069, 0.89493741, 0.23294199],
           [0.16184713, 0.89952218, 0.22632235],
           [0.16486861, 0.90411059, 0.21940008],
           [0.16803739, 0.90870282, 0.21214543],
           [0.17134592, 0.91329907, 0.20452294],
           [0.17478684, 0.91789950, 0.19648986],
           [0.17835305, 0.92250430, 0.18799392],
           [0.18203775, 0.92711366, 0.17897016],
           [0.18583441, 0.93172773, 0.16933626],
           [0.18973687, 0.93634671, 0.15898537],
           [0.19373925, 0.94097074, 0.14777467],
           [0.19783707, 0.94559983, 0.13551472],
           [0.20202413, 0.95023428, 0.12191216],
           [0.20629546, 0.95487427, 0.10651955],
           [0.21064650, 0.95951996, 0.08857277],
           [0.21507297, 0.96417151, 0.06655194]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.tree', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
