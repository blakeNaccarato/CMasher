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
cm_data = [[0.07720147, 0.07878641, 0.00250023],
           [0.08006543, 0.08272109, 0.00301507],
           [0.08288946, 0.08663908, 0.00355692],
           [0.08567420, 0.09054181, 0.00412465],
           [0.08842125, 0.09443017, 0.00471799],
           [0.09113142, 0.09830527, 0.00533613],
           [0.09380549, 0.10216811, 0.00597833],
           [0.09644470, 0.10601942, 0.00664432],
           [0.09904930, 0.10986025, 0.00733303],
           [0.10162032, 0.11369125, 0.00804420],
           [0.10415855, 0.11751309, 0.00877741],
           [0.10666396, 0.12132672, 0.00953152],
           [0.10913762, 0.12513258, 0.01030653],
           [0.11158002, 0.12893129, 0.01110198],
           [0.11399108, 0.13272364, 0.01191680],
           [0.11637161, 0.13651003, 0.01275098],
           [0.11872202, 0.14029097, 0.01360413],
           [0.12104238, 0.14406707, 0.01447556],
           [0.12333285, 0.14783886, 0.01536471],
           [0.12559400, 0.15160667, 0.01627154],
           [0.12782602, 0.15537097, 0.01719565],
           [0.13002889, 0.15913225, 0.01813647],
           [0.13220263, 0.16289098, 0.01909346],
           [0.13434766, 0.16664744, 0.02006667],
           [0.13646405, 0.17040201, 0.02105578],
           [0.13855187, 0.17415507, 0.02206048],
           [0.14061112, 0.17790699, 0.02308047],
           [0.14264149, 0.18165822, 0.02411509],
           [0.14464334, 0.18540896, 0.02516455],
           [0.14661661, 0.18915955, 0.02622864],
           [0.14856125, 0.19291029, 0.02730716],
           [0.15047718, 0.19666150, 0.02839994],
           [0.15236429, 0.20041346, 0.02950685],
           [0.15422247, 0.20416646, 0.03062776],
           [0.15605157, 0.20792077, 0.03176259],
           [0.15785143, 0.21167668, 0.03291126],
           [0.15962186, 0.21543443, 0.03407373],
           [0.16136267, 0.21919429, 0.03525002],
           [0.16307363, 0.22295651, 0.03644013],
           [0.16475451, 0.22672132, 0.03764413],
           [0.16640505, 0.23048896, 0.03886211],
           [0.16802497, 0.23425966, 0.04009419],
           [0.16961398, 0.23803365, 0.04132002],
           [0.17117177, 0.24181115, 0.04253333],
           [0.17269800, 0.24559236, 0.04373969],
           [0.17419233, 0.24937749, 0.04493961],
           [0.17565431, 0.25316677, 0.04613354],
           [0.17708309, 0.25696053, 0.04732146],
           [0.17847874, 0.26075884, 0.04850451],
           [0.17984081, 0.26456186, 0.04968326],
           [0.18116888, 0.26836979, 0.05085831],
           [0.18246177, 0.27218301, 0.05202944],
           [0.18371935, 0.27600158, 0.05319773],
           [0.18494139, 0.27982560, 0.05436414],
           [0.18612663, 0.28365544, 0.05552853],
           [0.18727460, 0.28749122, 0.05669172],
           [0.18838529, 0.29133296, 0.05785505],
           [0.18945648, 0.29518123, 0.05901759],
           [0.19048908, 0.29903578, 0.06018171],
           [0.19148092, 0.30289714, 0.06134674],
           [0.19243239, 0.30676518, 0.06251459],
           [0.19334128, 0.31064041, 0.06368472],
           [0.19420808, 0.31452265, 0.06485925],
           [0.19503040, 0.31841243, 0.06603769],
           [0.19580813, 0.32230969, 0.06722170],
           [0.19654036, 0.32621457, 0.06841231],
           [0.19722488, 0.33012750, 0.06960954],
           [0.19786115, 0.33404849, 0.07081491],
           [0.19844805, 0.33797768, 0.07202957],
           [0.19898412, 0.34191526, 0.07325449],
           [0.19946785, 0.34586145, 0.07449071],
           [0.19989766, 0.34981641, 0.07573938],
           [0.20027190, 0.35378035, 0.07700172],
           [0.20058887, 0.35775343, 0.07827907],
           [0.20084680, 0.36173584, 0.07957287],
           [0.20104385, 0.36572771, 0.08088469],
           [0.20117815, 0.36972921, 0.08221623],
           [0.20124774, 0.37374047, 0.08356934],
           [0.20124919, 0.37776190, 0.08494521],
           [0.20118102, 0.38179347, 0.08634642],
           [0.20104063, 0.38583536, 0.08777516],
           [0.20082453, 0.38988789, 0.08923341],
           [0.20053009, 0.39395115, 0.09072393],
           [0.20015455, 0.39802524, 0.09224976],
           [0.19969372, 0.40211047, 0.09381361],
           [0.19914361, 0.40620705, 0.09541880],
           [0.19850082, 0.41031504, 0.09706936],
           [0.19776051, 0.41443468, 0.09876928],
           [0.19691761, 0.41856620, 0.10052316],
           [0.19596819, 0.42270952, 0.10233672],
           [0.19490542, 0.42686501, 0.10421555],
           [0.19372449, 0.43103255, 0.10616692],
           [0.19241792, 0.43521239, 0.10819854],
           [0.19097830, 0.43940461, 0.11031968],
           [0.18939870, 0.44360905, 0.11254150],
           [0.18767246, 0.44782535, 0.11487735],
           [0.18579023, 0.45205339, 0.11734293],
           [0.18374374, 0.45629259, 0.11995780],
           [0.18152798, 0.46054169, 0.12274652],
           [0.17913880, 0.46479900, 0.12573996],
           [0.17657812, 0.46906167, 0.12897782],
           [0.17386176, 0.47332475, 0.13251164],
           [0.17102934, 0.47758005, 0.13640823],
           [0.16816973, 0.48181350, 0.14075162],
           [0.16546059, 0.48600155, 0.14563742],
           [0.16321947, 0.49010758, 0.15114398],
           [0.16190031, 0.49408552, 0.15726860],
           [0.16192858, 0.49789886, 0.16387320],
           [0.16346143, 0.50154176, 0.17073136],
           [0.16635281, 0.50503637, 0.17764590],
           [0.17032112, 0.50841392, 0.18450169],
           [0.17508991, 0.51170213, 0.19124822],
           [0.18043825, 0.51492201, 0.19787176],
           [0.18620136, 0.51808891, 0.20437270],
           [0.19226018, 0.52121384, 0.21075931],
           [0.19852782, 0.52430503, 0.21704043],
           [0.20494195, 0.52736850, 0.22322641],
           [0.21145591, 0.53040907, 0.22932549],
           [0.21803685, 0.53343025, 0.23534697],
           [0.22465903, 0.53643508, 0.24129752],
           [0.23130368, 0.53942597, 0.24718358],
           [0.23795717, 0.54240484, 0.25301126],
           [0.24460908, 0.54537335, 0.25878567],
           [0.25125141, 0.54833295, 0.26451120],
           [0.25787815, 0.55128490, 0.27019175],
           [0.26448539, 0.55423019, 0.27583125],
           [0.27106997, 0.55716977, 0.28143292],
           [0.27762972, 0.56010446, 0.28699977],
           [0.28416254, 0.56303512, 0.29253399],
           [0.29066805, 0.56596231, 0.29803850],
           [0.29714572, 0.56888662, 0.30351554],
           [0.30359475, 0.57180874, 0.30896670],
           [0.31001562, 0.57472907, 0.31439421],
           [0.31640859, 0.57764809, 0.31979984],
           [0.32277328, 0.58056639, 0.32518461],
           [0.32911075, 0.58348426, 0.33055046],
           [0.33542144, 0.58640211, 0.33589867],
           [0.34170590, 0.58932032, 0.34123048],
           [0.34796473, 0.59223924, 0.34654703],
           [0.35419861, 0.59515922, 0.35184943],
           [0.36040823, 0.59808057, 0.35713871],
           [0.36659430, 0.60100358, 0.36241586],
           [0.37275755, 0.60392854, 0.36768182],
           [0.37889858, 0.60685575, 0.37293736],
           [0.38501794, 0.60978554, 0.37818319],
           [0.39111663, 0.61271807, 0.38342032],
           [0.39719535, 0.61565359, 0.38864951],
           [0.40325434, 0.61859246, 0.39387113],
           [0.40929461, 0.62153481, 0.39908612],
           [0.41531682, 0.62448088, 0.40429514],
           [0.42132121, 0.62743099, 0.40949850],
           [0.42730892, 0.63038520, 0.41469720],
           [0.43327990, 0.63334392, 0.41989134],
           [0.43923537, 0.63630717, 0.42508192],
           [0.44517525, 0.63927534, 0.43026899],
           [0.45110064, 0.64224846, 0.43545349],
           [0.45701159, 0.64522687, 0.44063554],
           [0.46290890, 0.64821067, 0.44581586],
           [0.46879298, 0.65120008, 0.45099481],
           [0.47466415, 0.65419533, 0.45617275],
           [0.48052311, 0.65719654, 0.46135028],
           [0.48637009, 0.66020394, 0.46652767],
           [0.49220555, 0.66321772, 0.47170535],
           [0.49803002, 0.66623802, 0.47688381],
           [0.50384379, 0.66926504, 0.48206337],
           [0.50964717, 0.67229899, 0.48724435],
           [0.51544067, 0.67533998, 0.49242724],
           [0.52122463, 0.67838821, 0.49761239],
           [0.52699929, 0.68144388, 0.50280009],
           [0.53276501, 0.68450714, 0.50799072],
           [0.53852217, 0.68757815, 0.51318468],
           [0.54427106, 0.69065708, 0.51838230],
           [0.55001196, 0.69374410, 0.52358393],
           [0.55574508, 0.69683941, 0.52878985],
           [0.56147078, 0.69994314, 0.53400046],
           [0.56718932, 0.70305546, 0.53921610],
           [0.57290094, 0.70617653, 0.54443711],
           [0.57860588, 0.70930653, 0.54966380],
           [0.58430433, 0.71244564, 0.55489649],
           [0.58999654, 0.71559400, 0.56013554],
           [0.59568274, 0.71875177, 0.56538128],
           [0.60136312, 0.72191914, 0.57063405],
           [0.60703787, 0.72509625, 0.57589418],
           [0.61270717, 0.72828328, 0.58116200],
           [0.61837118, 0.73148040, 0.58643785],
           [0.62403008, 0.73468776, 0.59172207],
           [0.62968401, 0.73790555, 0.59701500],
           [0.63533311, 0.74113392, 0.60231699],
           [0.64097752, 0.74437305, 0.60762838],
           [0.64661736, 0.74762310, 0.61294953],
           [0.65225274, 0.75088425, 0.61828078],
           [0.65788378, 0.75415667, 0.62362252],
           [0.66351054, 0.75744054, 0.62897508],
           [0.66913312, 0.76073602, 0.63433885],
           [0.67475157, 0.76404331, 0.63971417],
           [0.68036595, 0.76736259, 0.64510145],
           [0.68597634, 0.77069401, 0.65050109],
           [0.69158276, 0.77403778, 0.65591347],
           [0.69718520, 0.77739409, 0.66133897],
           [0.70278368, 0.78076313, 0.66677799],
           [0.70837818, 0.78414510, 0.67223095],
           [0.71396876, 0.78754017, 0.67769833],
           [0.71955533, 0.79094855, 0.68318052],
           [0.72513781, 0.79437046, 0.68867794],
           [0.73071614, 0.79780612, 0.69419101],
           [0.73629030, 0.80125570, 0.69972030],
           [0.74186018, 0.80471944, 0.70526622],
           [0.74742558, 0.80819759, 0.71082920],
           [0.75298640, 0.81169038, 0.71640975],
           [0.75854259, 0.81519797, 0.72200850],
           [0.76409382, 0.81872069, 0.72762578],
           [0.76963991, 0.82225878, 0.73326215],
           [0.77518077, 0.82581244, 0.73891829],
           [0.78071598, 0.82938200, 0.74459454],
           [0.78624535, 0.83296771, 0.75029158],
           [0.79176859, 0.83656985, 0.75600996],
           [0.79728526, 0.84018876, 0.76175013],
           [0.80279519, 0.84382466, 0.76751292],
           [0.80829772, 0.84747799, 0.77329856],
           [0.81379273, 0.85114893, 0.77910805],
           [0.81927945, 0.85483800, 0.78494155],
           [0.82475767, 0.85854539, 0.79080004],
           [0.83022662, 0.86227162, 0.79668374],
           [0.83568588, 0.86601699, 0.80259345],
           [0.84113479, 0.86978194, 0.80852963],
           [0.84657264, 0.87356693, 0.81449264],
           [0.85199894, 0.87737231, 0.82048327],
           [0.85741286, 0.88119862, 0.82650168],
           [0.86281364, 0.88504634, 0.83254820],
           [0.86820057, 0.88891596, 0.83862311],
           [0.87357297, 0.89280794, 0.84472671],
           [0.87892998, 0.89672288, 0.85085878],
           [0.88427084, 0.90066132, 0.85701914],
           [0.88959483, 0.90462383, 0.86320733],
           [0.89490126, 0.90861098, 0.86942262],
           [0.90018953, 0.91262336, 0.87566391],
           [0.90545908, 0.91666158, 0.88192965],
           [0.91070951, 0.92072626, 0.88821774],
           [0.91594052, 0.92481804, 0.89452541],
           [0.92115193, 0.92893757, 0.90084910],
           [0.92634371, 0.93308560, 0.90718433],
           [0.93151582, 0.93726294, 0.91352553],
           [0.93666816, 0.94147055, 0.91986610],
           [0.94180023, 0.94570970, 0.92619816],
           [0.94691080, 0.94998202, 0.93251287],
           [0.95199740, 0.95428971, 0.93880101],
           [0.95705572, 0.95863561, 0.94505383],
           [0.96207918, 0.96302331, 0.95126442],
           [0.96705890, 0.96745691, 0.95742940],
           [0.97198437, 0.97194065, 0.96355059],
           [0.97684502, 0.97647819, 0.96963549],
           [0.98163215, 0.98107190, 0.97569666],
           [0.98634054, 0.98572246, 0.98174951],
           [0.99096917, 0.99042891, 0.98780949],
           [0.99552062, 0.99518904, 0.99388975],
           [1.00000000, 1.00000000, 1.00000000],
           [0.99654697, 0.99471962, 0.99451894],
           [0.99308247, 0.98946529, 0.98906751],
           [0.98960586, 0.98423715, 0.98364553],
           [0.98611531, 0.97903575, 0.97825327],
           [0.98260827, 0.97386194, 0.97289121],
           [0.97908248, 0.96871648, 0.96755942],
           [0.97553257, 0.96360128, 0.96225909],
           [0.97195276, 0.95851847, 0.95699102],
           [0.96833050, 0.95347261, 0.95175884],
           [0.96464441, 0.94847108, 0.94657353],
           [0.96086609, 0.94351980, 0.94148763],
           [0.95716222, 0.93854294, 0.93658459],
           [0.95384749, 0.93344032, 0.93160396],
           [0.95076567, 0.92828339, 0.92645470],
           [0.94779809, 0.92311086, 0.92121873],
           [0.94490652, 0.91793320, 0.91593925],
           [0.94207508, 0.91275441, 0.91063593],
           [0.93929445, 0.90757681, 0.90531923],
           [0.93655880, 0.90240179, 0.89999523],
           [0.93386378, 0.89723041, 0.89466791],
           [0.93120579, 0.89206350, 0.88934015],
           [0.92858261, 0.88690148, 0.88401374],
           [0.92599115, 0.88174514, 0.87869062],
           [0.92343074, 0.87659437, 0.87337140],
           [0.92089821, 0.87145004, 0.86805775],
           [0.91839365, 0.86631181, 0.86274975],
           [0.91591451, 0.86118032, 0.85744863],
           [0.91346016, 0.85605555, 0.85215469],
           [0.91102973, 0.85093754, 0.84686833],
           [0.90862134, 0.84582672, 0.84159038],
           [0.90623559, 0.84072260, 0.83632049],
           [0.90387032, 0.83562573, 0.83105959],
           [0.90152498, 0.83053608, 0.82580786],
           [0.89919973, 0.82545331, 0.82056513],
           [0.89689268, 0.82037791, 0.81533218],
           [0.89460369, 0.81530968, 0.81010898],
           [0.89233264, 0.81024841, 0.80489546],
           [0.89007800, 0.80519445, 0.79969225],
           [0.88783948, 0.80014768, 0.79449936],
           [0.88561738, 0.79510773, 0.78931654],
           [0.88341011, 0.79007497, 0.78414442],
           [0.88121723, 0.78504936, 0.77898311],
           [0.87903903, 0.78003052, 0.77383235],
           [0.87687465, 0.77501856, 0.76869243],
           [0.87472328, 0.77001358, 0.76356362],
           [0.87258453, 0.76501549, 0.75844601],
           [0.87045854, 0.76002399, 0.75333941],
           [0.86834471, 0.75503910, 0.74824401],
           [0.86624226, 0.75006088, 0.74316006],
           [0.86415083, 0.74508927, 0.73808765],
           [0.86207005, 0.74012418, 0.73302683],
           [0.85999986, 0.73516539, 0.72797755],
           [0.85793996, 0.73021280, 0.72293985],
           [0.85588960, 0.72526648, 0.71791399],
           [0.85384843, 0.72032634, 0.71290005],
           [0.85181614, 0.71539229, 0.70789810],
           [0.84979237, 0.71046424, 0.70290821],
           [0.84777681, 0.70554209, 0.69793046],
           [0.84576913, 0.70062575, 0.69296493],
           [0.84376902, 0.69571512, 0.68801169],
           [0.84177614, 0.69081010, 0.68307082],
           [0.83979023, 0.68591057, 0.67814239],
           [0.83781096, 0.68101645, 0.67322650],
           [0.83583792, 0.67612767, 0.66832326],
           [0.83387081, 0.67124413, 0.66343279],
           [0.83190933, 0.66636573, 0.65855516],
           [0.82995330, 0.66149231, 0.65369041],
           [0.82800231, 0.65662380, 0.64883870],
           [0.82605606, 0.65176012, 0.64400014],
           [0.82411424, 0.64690115, 0.63917483],
           [0.82217652, 0.64204681, 0.63436291],
           [0.82024260, 0.63719699, 0.62956449],
           [0.81831216, 0.63235159, 0.62477972],
           [0.81638489, 0.62751053, 0.62000872],
           [0.81446048, 0.62267368, 0.61525163],
           [0.81253936, 0.61784059, 0.61050825],
           [0.81062051, 0.61301151, 0.60577908],
           [0.80870359, 0.60818634, 0.60106428],
           [0.80678828, 0.60336499, 0.59636402],
           [0.80487505, 0.59854696, 0.59167810],
           [0.80296309, 0.59373238, 0.58700695],
           [0.80105180, 0.58892133, 0.58235089],
           [0.79914151, 0.58411333, 0.57770980],
           [0.79723187, 0.57930830, 0.57308391],
           [0.79532190, 0.57450651, 0.56847375],
           [0.79341260, 0.56970712, 0.56387892],
           [0.79150248, 0.56491065, 0.55930021],
           [0.78959202, 0.56011657, 0.55473748],
           [0.78768056, 0.55532494, 0.55019115],
           [0.78576809, 0.55053548, 0.54566134],
           [0.78385402, 0.54574822, 0.54114845],
           [0.78193863, 0.54096271, 0.53665249],
           [0.78002073, 0.53617932, 0.53217417],
           [0.77810134, 0.53139714, 0.52771319],
           [0.77617914, 0.52661664, 0.52327034],
           [0.77425387, 0.52183765, 0.51884592],
           [0.77232613, 0.51705948, 0.51443990],
           [0.77039499, 0.51228237, 0.51005292],
           [0.76846011, 0.50750618, 0.50568540],
           [0.76652128, 0.50273069, 0.50133768],
           [0.76457829, 0.49795571, 0.49701018],
           [0.76263093, 0.49318098, 0.49270330],
           [0.76067901, 0.48840628, 0.48841748],
           [0.75872201, 0.48363156, 0.48415332],
           [0.75675963, 0.47885663, 0.47991134],
           [0.75479180, 0.47408116, 0.47569202],
           [0.75281808, 0.46930503, 0.47149602],
           [0.75083807, 0.46452810, 0.46732401],
           [0.74885135, 0.45975024, 0.46317671],
           [0.74685747, 0.45497133, 0.45905489],
           [0.74485677, 0.45019070, 0.45495908],
           [0.74284827, 0.44540857, 0.45089035],
           [0.74083157, 0.44062476, 0.44684961],
           [0.73880677, 0.43583872, 0.44283766],
           [0.73677293, 0.43105063, 0.43885572],
           [0.73472975, 0.42626021, 0.43490488],
           [0.73267721, 0.42146694, 0.43098622],
           [0.73061426, 0.41667105, 0.42710124],
           [0.72854053, 0.41187228, 0.42325133],
           [0.72645553, 0.40707040, 0.41943804],
           [0.72435865, 0.40226528, 0.41566308],
           [0.72224919, 0.39745684, 0.41192833],
           [0.72012632, 0.39264510, 0.40823589],
           [0.71798939, 0.38782987, 0.40458796],
           [0.71583766, 0.38301106, 0.40098702],
           [0.71366972, 0.37818908, 0.39743591],
           [0.71148462, 0.37336395, 0.39393767],
           [0.70928139, 0.36853569, 0.39049568],
           [0.70705818, 0.36370500, 0.38711378],
           [0.70481333, 0.35887247, 0.38379625],
           [0.70254531, 0.35403847, 0.38054787],
           [0.70025129, 0.34920457, 0.37737404],
           [0.69792897, 0.34437182, 0.37428086],
           [0.69557489, 0.33954231, 0.37127518],
           [0.69318533, 0.33471840, 0.36836478],
           [0.69075550, 0.32990345, 0.36555835],
           [0.68828038, 0.32510108, 0.36286584],
           [0.68575270, 0.32031720, 0.36029808],
           [0.68316437, 0.31555864, 0.35786705],
           [0.68050576, 0.31083404, 0.35558578],
           [0.67776485, 0.30615481, 0.35346748],
           [0.67492789, 0.30153473, 0.35152516],
           [0.67197917, 0.29699044, 0.34977014],
           [0.66890167, 0.29254116, 0.34821023],
           [0.66567827, 0.28820769, 0.34684754],
           [0.66229362, 0.28401072, 0.34567632],
           [0.65873645, 0.27996826, 0.34468212],
           [0.65500145, 0.27609335, 0.34384190],
           [0.65109026, 0.27239212, 0.34312689],
           [0.64701105, 0.26886361, 0.34250580],
           [0.64277687, 0.26550065, 0.34194872],
           [0.63840361, 0.26229186, 0.34142896],
           [0.63390801, 0.25922354, 0.34092501],
           [0.62930636, 0.25628130, 0.34041987],
           [0.62461360, 0.25345114, 0.33990104],
           [0.61984305, 0.25072008, 0.33935940],
           [0.61500621, 0.24807645, 0.33878871],
           [0.61011300, 0.24550994, 0.33818470],
           [0.60517198, 0.24301141, 0.33754427],
           [0.60019020, 0.24057307, 0.33686606],
           [0.59517383, 0.23818803, 0.33614897],
           [0.59012810, 0.23585033, 0.33539255],
           [0.58505744, 0.23355477, 0.33459681],
           [0.57996562, 0.23129686, 0.33376205],
           [0.57485609, 0.22907247, 0.33288833],
           [0.56973151, 0.22687824, 0.33197651],
           [0.56459439, 0.22471102, 0.33102706],
           [0.55944692, 0.22256803, 0.33004052],
           [0.55429099, 0.22044681, 0.32901750],
           [0.54912824, 0.21834515, 0.32795864],
           [0.54396011, 0.21626111, 0.32686460],
           [0.53878783, 0.21419293, 0.32573606],
           [0.53361258, 0.21213897, 0.32457353],
           [0.52843544, 0.21009770, 0.32337749],
           [0.52325718, 0.20806790, 0.32214866],
           [0.51807873, 0.20604825, 0.32088738],
           [0.51290076, 0.20403765, 0.31959422],
           [0.50772387, 0.20203513, 0.31826969],
           [0.50254868, 0.20003967, 0.31691417],
           [0.49737578, 0.19805036, 0.31552800],
           [0.49220556, 0.19606642, 0.31411167],
           [0.48703845, 0.19408709, 0.31266552],
           [0.48187483, 0.19211166, 0.31118990],
           [0.47671506, 0.19013944, 0.30968513],
           [0.47155944, 0.18816980, 0.30815151],
           [0.46640825, 0.18620218, 0.30658933],
           [0.46126175, 0.18423597, 0.30499883],
           [0.45612020, 0.18227064, 0.30338022],
           [0.45098375, 0.18030573, 0.30173380],
           [0.44585257, 0.17834077, 0.30005979],
           [0.44072683, 0.17637530, 0.29835838],
           [0.43560676, 0.17440880, 0.29662966],
           [0.43049237, 0.17244096, 0.29487390],
           [0.42538380, 0.17047137, 0.29309126],
           [0.42028123, 0.16849957, 0.29128178],
           [0.41518462, 0.16652527, 0.28944570],
           [0.41009413, 0.16454806, 0.28758306],
           [0.40500978, 0.16256763, 0.28569400],
           [0.39993162, 0.16058363, 0.28377860],
           [0.39485970, 0.15859571, 0.28183694],
           [0.38979405, 0.15660359, 0.27986909],
           [0.38473467, 0.15460692, 0.27787511],
           [0.37968158, 0.15260542, 0.27585504],
           [0.37463477, 0.15059878, 0.27380893],
           [0.36959426, 0.14858669, 0.27173678],
           [0.36455998, 0.14656890, 0.26963864],
           [0.35953198, 0.14454505, 0.26751447],
           [0.35451016, 0.14251492, 0.26536431],
           [0.34949452, 0.14047819, 0.26318813],
           [0.34448500, 0.13843458, 0.26098589],
           [0.33948154, 0.13638382, 0.25875758],
           [0.33448410, 0.13432561, 0.25650314],
           [0.32949260, 0.13225968, 0.25422251],
           [0.32450695, 0.13018575, 0.25191564],
           [0.31952709, 0.12810350, 0.24958244],
           [0.31455293, 0.12601267, 0.24722284],
           [0.30958436, 0.12391297, 0.24483674],
           [0.30462129, 0.12180408, 0.24242401],
           [0.29966361, 0.11968572, 0.23998456],
           [0.29471119, 0.11755757, 0.23751825],
           [0.28976392, 0.11541932, 0.23502494],
           [0.28482165, 0.11327066, 0.23250448],
           [0.27988426, 0.11111126, 0.22995670],
           [0.27495159, 0.10894078, 0.22738143],
           [0.27002349, 0.10675889, 0.22477848],
           [0.26509979, 0.10456521, 0.22214764],
           [0.26018030, 0.10235940, 0.21948870],
           [0.25526487, 0.10014107, 0.21680143],
           [0.25035330, 0.09790983, 0.21408558],
           [0.24544536, 0.09566528, 0.21134090],
           [0.24054086, 0.09340699, 0.20856710],
           [0.23563958, 0.09113453, 0.20576389],
           [0.23074126, 0.08884744, 0.20293097],
           [0.22584569, 0.08654522, 0.20006800],
           [0.22095258, 0.08422739, 0.19717464],
           [0.21606167, 0.08189341, 0.19425052],
           [0.21117268, 0.07954271, 0.19129524],
           [0.20628527, 0.07717473, 0.18830843],
           [0.20139919, 0.07478882, 0.18528961],
           [0.19651402, 0.07238434, 0.18223835],
           [0.19162949, 0.06996056, 0.17915416],
           [0.18674517, 0.06751676, 0.17603654],
           [0.18186070, 0.06505212, 0.17288495],
           [0.17697564, 0.06256578, 0.16969883],
           [0.17208959, 0.06005681, 0.16647757],
           [0.16720205, 0.05752423, 0.16322056],
           [0.16231256, 0.05496692, 0.15992712],
           [0.15742056, 0.05238376, 0.15659656],
           [0.15252557, 0.04977339, 0.15322815],
           [0.14762692, 0.04713449, 0.14982112],
           [0.14272405, 0.04446544, 0.14637463],
           [0.13781629, 0.04176455, 0.14288784],
           [0.13290288, 0.03902073, 0.13935985],
           [0.12798314, 0.03631810, 0.13578971],
           [0.12305625, 0.03369292, 0.13217641]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.holly', N=511)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
