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
cm_data = [[0.56455228, 0.05411374, 0.64628069],
           [0.56944818, 0.05368478, 0.64276375],
           [0.57434602, 0.05314874, 0.63921671],
           [0.57924515, 0.05250974, 0.63563620],
           [0.58414518, 0.05177101, 0.63201829],
           [0.58904474, 0.05093764, 0.62836101],
           [0.59394345, 0.05001254, 0.62466046],
           [0.59884006, 0.04900039, 0.62091449],
           [0.60373382, 0.04790475, 0.61711990],
           [0.60862359, 0.04673015, 0.61327438],
           [0.61350851, 0.04548060, 0.60937502],
           [0.61838721, 0.04416151, 0.60542001],
           [0.62325899, 0.04277693, 0.60140609],
           [0.62812219, 0.04133374, 0.59733216],
           [0.63297595, 0.03982967, 0.59319535],
           [0.63781889, 0.03829265, 0.58899395],
           [0.64264953, 0.03675466, 0.58472657],
           [0.64746668, 0.03522607, 0.58039113],
           [0.65226902, 0.03371776, 0.57598584],
           [0.65705489, 0.03224182, 0.57150985],
           [0.66182280, 0.03081001, 0.56696189],
           [0.66657121, 0.02943445, 0.56234081],
           [0.67129853, 0.02812765, 0.55764566],
           [0.67600321, 0.02690227, 0.55287541],
           [0.68068345, 0.02577189, 0.54802973],
           [0.68533748, 0.02475027, 0.54310825],
           [0.68996351, 0.02385154, 0.53811074],
           [0.69455968, 0.02309028, 0.53303718],
           [0.69912410, 0.02248146, 0.52788771],
           [0.70365492, 0.02204027, 0.52266239],
           [0.70815008, 0.02178275, 0.51736197],
           [0.71260754, 0.02172528, 0.51198731],
           [0.71702522, 0.02188464, 0.50653942],
           [0.72140099, 0.02227802, 0.50101956],
           [0.72573281, 0.02292279, 0.49542874],
           [0.73001853, 0.02383700, 0.48976861],
           [0.73425579, 0.02503938, 0.48404156],
           [0.73844250, 0.02654848, 0.47824923],
           [0.74257644, 0.02838346, 0.47239388],
           [0.74665521, 0.03056407, 0.46647869],
           [0.75067679, 0.03310966, 0.46050537],
           [0.75463868, 0.03604071, 0.45447817],
           [0.75853889, 0.03937705, 0.44839910],
           [0.76237498, 0.04304459, 0.44227269],
           [0.76614490, 0.04692205, 0.43610189],
           [0.76984645, 0.05100055, 0.42989086],
           [0.77347747, 0.05526275, 0.42364388],
           [0.77703604, 0.05969260, 0.41736452],
           [0.78052008, 0.06427545, 0.41105769],
           [0.78392770, 0.06899791, 0.40472794],
           [0.78725713, 0.07384778, 0.39837975],
           [0.79050667, 0.07881402, 0.39201764],
           [0.79367470, 0.08388646, 0.38564673],
           [0.79675976, 0.08905583, 0.37927182],
           [0.79976051, 0.09431365, 0.37289773],
           [0.80267575, 0.09965207, 0.36652927],
           [0.80550444, 0.10506387, 0.36017120],
           [0.80824566, 0.11054230, 0.35382818],
           [0.81089868, 0.11608107, 0.34750486],
           [0.81346290, 0.12167429, 0.34120571],
           [0.81593790, 0.12731644, 0.33493497],
           [0.81832340, 0.13300231, 0.32869674],
           [0.82061930, 0.13872703, 0.32249484],
           [0.82282562, 0.14448597, 0.31633290],
           [0.82494256, 0.15027477, 0.31021425],
           [0.82697044, 0.15608933, 0.30414196],
           [0.82890971, 0.16192577, 0.29811878],
           [0.83076096, 0.16778046, 0.29214719],
           [0.83252488, 0.17364996, 0.28622935],
           [0.83420228, 0.17953105, 0.28036713],
           [0.83579403, 0.18542075, 0.27456203],
           [0.83730109, 0.19131627, 0.26881525],
           [0.83872451, 0.19721502, 0.26312771],
           [0.84006537, 0.20311461, 0.25750001],
           [0.84132480, 0.20901284, 0.25193246],
           [0.84250398, 0.21490764, 0.24642520],
           [0.84360412, 0.22079711, 0.24097808],
           [0.84462640, 0.22667967, 0.23559052],
           [0.84557203, 0.23255381, 0.23026180],
           [0.84644220, 0.23841815, 0.22499105],
           [0.84723819, 0.24427132, 0.21977746],
           [0.84796109, 0.25011245, 0.21461939],
           [0.84861202, 0.25594061, 0.20951537],
           [0.84919225, 0.26175472, 0.20446427],
           [0.84970271, 0.26755435, 0.19946387],
           [0.85014449, 0.27333884, 0.19451245],
           [0.85051865, 0.27910758, 0.18960826],
           [0.85082598, 0.28486043, 0.18474878],
           [0.85106762, 0.29059669, 0.17993253],
           [0.85124415, 0.29631659, 0.17515656],
           [0.85135664, 0.30201950, 0.17041934],
           [0.85140556, 0.30770579, 0.16571782],
           [0.85139186, 0.31337501, 0.16105031],
           [0.85131595, 0.31902750, 0.15641389],
           [0.85117852, 0.32466319, 0.15180640],
           [0.85098010, 0.33028216, 0.14722544],
           [0.85072104, 0.33588475, 0.14266829],
           [0.85040192, 0.34147090, 0.13813290],
           [0.85002300, 0.34704095, 0.13361666],
           [0.84958455, 0.35259523, 0.12911701],
           [0.84908687, 0.35813391, 0.12463171],
           [0.84853026, 0.36365717, 0.12015859],
           [0.84791475, 0.36916547, 0.11569506],
           [0.84724045, 0.37465912, 0.11123888],
           [0.84650743, 0.38013842, 0.10678790],
           [0.84571579, 0.38560359, 0.10234018],
           [0.84486550, 0.39105501, 0.09789367],
           [0.84395643, 0.39649305, 0.09344641],
           [0.84298849, 0.40191804, 0.08899672],
           [0.84196153, 0.40733030, 0.08454308],
           [0.84087540, 0.41273015, 0.08008424],
           [0.83972988, 0.41811790, 0.07561925],
           [0.83852473, 0.42349386, 0.07114753],
           [0.83725967, 0.42885833, 0.06666897],
           [0.83593441, 0.43421159, 0.06218408],
           [0.83454862, 0.43955392, 0.05769412],
           [0.83310194, 0.44488559, 0.05320136],
           [0.83159399, 0.45020686, 0.04870934],
           [0.83002435, 0.45551796, 0.04422324],
           [0.82839261, 0.46081911, 0.03974216],
           [0.82669832, 0.46611053, 0.03540953],
           [0.82494100, 0.47139241, 0.03139860],
           [0.82312017, 0.47666492, 0.02771200],
           [0.82123534, 0.48192824, 0.02435299],
           [0.81928597, 0.48718251, 0.02132545],
           [0.81727153, 0.49242785, 0.01863384],
           [0.81519149, 0.49766439, 0.01628324],
           [0.81304526, 0.50289221, 0.01427932],
           [0.81083233, 0.50811136, 0.01262838],
           [0.80855209, 0.51332192, 0.01133724],
           [0.80620390, 0.51852397, 0.01041329],
           [0.80378714, 0.52371753, 0.00986456],
           [0.80130120, 0.52890263, 0.00969965],
           [0.79874541, 0.53407928, 0.00992776],
           [0.79611913, 0.53924747, 0.01055866],
           [0.79342175, 0.54440712, 0.01160276],
           [0.79065251, 0.54955827, 0.01307100],
           [0.78781070, 0.55470087, 0.01497493],
           [0.78489559, 0.55983486, 0.01732677],
           [0.78190645, 0.56496019, 0.02013930],
           [0.77884252, 0.57007675, 0.02342598],
           [0.77570301, 0.57518449, 0.02720086],
           [0.77248708, 0.58028332, 0.03147870],
           [0.76919389, 0.58537316, 0.03627489],
           [0.76582256, 0.59045388, 0.04157678],
           [0.76237220, 0.59552539, 0.04704716],
           [0.75884188, 0.60058757, 0.05260930],
           [0.75523059, 0.60564031, 0.05825116],
           [0.75153734, 0.61068347, 0.06396368],
           [0.74776108, 0.61571693, 0.06974010],
           [0.74390069, 0.62074056, 0.07557546],
           [0.73995504, 0.62575421, 0.08146611],
           [0.73592294, 0.63075773, 0.08740952],
           [0.73180317, 0.63575097, 0.09340396],
           [0.72759444, 0.64073377, 0.09944836],
           [0.72329536, 0.64570597, 0.10554222],
           [0.71890457, 0.65066738, 0.11168542],
           [0.71442064, 0.65561782, 0.11787819],
           [0.70984205, 0.66055709, 0.12412104],
           [0.70516726, 0.66548496, 0.13041474],
           [0.70039460, 0.67040125, 0.13676024],
           [0.69552240, 0.67530570, 0.14315866],
           [0.69054897, 0.68019806, 0.14961124],
           [0.68547252, 0.68507803, 0.15611932],
           [0.68029123, 0.68994534, 0.16268439],
           [0.67500320, 0.69479965, 0.16930799],
           [0.66960646, 0.69964065, 0.17599179],
           [0.66409902, 0.70446796, 0.18273747],
           [0.65847892, 0.70928116, 0.18954675],
           [0.65274412, 0.71407982, 0.19642142],
           [0.64689253, 0.71886348, 0.20336329],
           [0.64092206, 0.72363162, 0.21037422],
           [0.63483059, 0.72838370, 0.21745606],
           [0.62861601, 0.73311914, 0.22461070],
           [0.62227614, 0.73783732, 0.23184004],
           [0.61580897, 0.74253753, 0.23914588],
           [0.60921244, 0.74721905, 0.24653006],
           [0.60248455, 0.75188108, 0.25399437],
           [0.59562335, 0.75652280, 0.26154056],
           [0.58862695, 0.76114331, 0.26917031],
           [0.58149359, 0.76574166, 0.27688525],
           [0.57422159, 0.77031683, 0.28468690],
           [0.56680942, 0.77486778, 0.29257670],
           [0.55925572, 0.77939336, 0.30055596],
           [0.55155928, 0.78389241, 0.30862585],
           [0.54371913, 0.78836367, 0.31678743],
           [0.53573450, 0.79280585, 0.32504155],
           [0.52760490, 0.79721761, 0.33338891],
           [0.51933015, 0.80159753, 0.34182998],
           [0.51091035, 0.80594418, 0.35036505],
           [0.50234597, 0.81025606, 0.35899416],
           [0.49363785, 0.81453165, 0.36771712],
           [0.48478724, 0.81876939, 0.37653346],
           [0.47579584, 0.82296771, 0.38544246],
           [0.46666582, 0.82712501, 0.39444311],
           [0.45739987, 0.83123971, 0.40353412],
           [0.44800120, 0.83531019, 0.41271388],
           [0.43847363, 0.83933488, 0.42198049],
           [0.42882156, 0.84331224, 0.43133175],
           [0.41905005, 0.84724072, 0.44076517],
           [0.40916483, 0.85111888, 0.45027794],
           [0.39917249, 0.85494527, 0.45986690],
           [0.38908045, 0.85871854, 0.46952857],
           [0.37889654, 0.86243745, 0.47925944],
           [0.36862966, 0.86610083, 0.48905566],
           [0.35828964, 0.86970762, 0.49891313],
           [0.34788725, 0.87325686, 0.50882760],
           [0.33743494, 0.87674768, 0.51879427],
           [0.32694603, 0.88017936, 0.52880839],
           [0.31643427, 0.88355138, 0.53886564],
           [0.30591537, 0.88686330, 0.54896129],
           [0.29540838, 0.89011474, 0.55908952],
           [0.28493164, 0.89330560, 0.56924602],
           [0.27450569, 0.89643592, 0.57942640],
           [0.26415720, 0.89950568, 0.58962406],
           [0.25390975, 0.90251531, 0.59983590],
           [0.24379475, 0.90546512, 0.61005610],
           [0.23384436, 0.90835570, 0.62028055],
           [0.22409624, 0.91118769, 0.63050437],
           [0.21459076, 0.91396191, 0.64072381],
           [0.20537615, 0.91667923, 0.65093355],
           [0.19650090, 0.91934070, 0.66113144],
           [0.18802519, 0.92194739, 0.67131172],
           [0.18000958, 0.92450052, 0.68147200],
           [0.17252068, 0.92700139, 0.69160949],
           [0.16563088, 0.92945133, 0.70172061],
           [0.15941552, 0.93185177, 0.71180153],
           [0.15394631, 0.93420419, 0.72185109],
           [0.14929371, 0.93651011, 0.73186693],
           [0.14552056, 0.93877108, 0.74184696],
           [0.14267763, 0.94098870, 0.75178939],
           [0.14079933, 0.94316460, 0.76169269],
           [0.13990036, 0.94530040, 0.77155565],
           [0.13997391, 0.94739774, 0.78137734],
           [0.14099175, 0.94945828, 0.79115709],
           [0.14290638, 0.95148365, 0.80089455],
           [0.14565463, 0.95347546, 0.81058963],
           [0.14916227, 0.95543533, 0.82024250],
           [0.15334884, 0.95736486, 0.82985328],
           [0.15813200, 0.95926575, 0.83942078],
           [0.16343017, 0.96113938, 0.84894778],
           [0.16916656, 0.96298723, 0.85843548],
           [0.17527005, 0.96481090, 0.86788344],
           [0.18167605, 0.96661184, 0.87729297],
           [0.18832745, 0.96839121, 0.88666775],
           [0.19517300, 0.97015069, 0.89600600],
           [0.20216919, 0.97189127, 0.90531247],
           [0.20927745, 0.97361437, 0.91458761],
           [0.21646507, 0.97532109, 0.92383407],
           [0.22370382, 0.97701262, 0.93305384],
           [0.23096998, 0.97868993, 0.94225002],
           [0.23824254, 0.98035424, 0.95142350],
           [0.24550556, 0.98200612, 0.96058006],
           [0.25274256, 0.98364704, 0.96971787],
           [0.25994303, 0.98527734, 0.97884366],
           [0.26709688, 0.98689776, 0.98796051]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.neon', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
