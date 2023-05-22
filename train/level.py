# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Level(KaitaiStruct):

    class AutoscrollSpeed(IntEnum):
        x1 = 0
        x2 = 1
        x3 = 2

    class ClearCondition(IntEnum):
        none = 0
        reach_the_goal_without_landing_after_leaving_the_ground = 137525990
        reach_the_goal_after_defeating_at_least_all_mechakoopa = 199585683
        reach_the_goal_after_defeating_at_least_all_cheep_cheep = 272349836
        reach_the_goal_without_taking_damage = 375673178
        reach_the_goal_as_boomerang_mario = 426197923
        reach_the_goal_while_wearing_a_shoe = 436833616
        reach_the_goal_as_fire_mario = 713979835
        reach_the_goal_as_frog_mario = 744927294
        reach_the_goal_after_defeating_at_least_all_larry = 751004331
        reach_the_goal_as_raccoon_mario = 900050759
        reach_the_goal_after_defeating_at_least_all_blooper = 947659466
        reach_the_goal_as_propeller_mario = 976173462
        reach_the_goal_while_wearing_a_propeller_box = 994686866
        reach_the_goal_after_defeating_at_least_all_spike = 998904081
        reach_the_goal_after_defeating_at_least_all_boom_boom = 1008094897
        reach_the_goal_while_holding_a_koopa_shell = 1051433633
        reach_the_goal_after_defeating_at_least_all_porcupuffer = 1061233896
        reach_the_goal_after_defeating_at_least_all_charvaargh = 1062253843
        reach_the_goal_after_defeating_at_least_all_bullet_bill = 1079889509
        reach_the_goal_after_defeating_at_least_all_bully_bullies = 1080535886
        reach_the_goal_while_wearing_a_goomba_mask = 1151250770
        reach_the_goal_after_defeating_at_least_all_hop_chops = 1182464856
        reach_the_goal_while_holding_a_red_pow_block_or_reach_the_goal_after_activating_at_least_all_red_pow_block = 1219761531
        reach_the_goal_after_defeating_at_least_all_bob_omb = 1221661152
        reach_the_goal_after_defeating_at_least_all_spiny_spinies = 1259427138
        reach_the_goal_after_defeating_at_least_all_bowser_meowser = 1268255615
        reach_the_goal_after_defeating_at_least_all_ant_trooper = 1279580818
        reach_the_goal_on_a_lakitus_cloud = 1283945123
        reach_the_goal_after_defeating_at_least_all_boo = 1344044032
        reach_the_goal_after_defeating_at_least_all_roy = 1425973877
        reach_the_goal_while_holding_a_trampoline = 1429902736
        reach_the_goal_after_defeating_at_least_all_morton = 1431944825
        reach_the_goal_after_defeating_at_least_all_fish_bone = 1446467058
        reach_the_goal_after_defeating_at_least_all_monty_mole = 1510495760
        reach_the_goal_after_picking_up_at_least_all_1_up_mushroom = 1656179347
        reach_the_goal_after_defeating_at_least_all_hammer_bro = 1665820273
        reach_the_goal_after_hitting_at_least_all_p_switch_or_reach_the_goal_while_holding_a_p_switch = 1676924210
        reach_the_goal_after_activating_at_least_all_pow_block_or_reach_the_goal_while_holding_a_pow_block = 1715960804
        reach_the_goal_after_defeating_at_least_all_angry_sun = 1724036958
        reach_the_goal_after_defeating_at_least_all_pokey = 1730095541
        reach_the_goal_as_superball_mario = 1780278293
        reach_the_goal_after_defeating_at_least_all_pom_pom = 1839897151
        reach_the_goal_after_defeating_at_least_all_peepa = 1969299694
        reach_the_goal_after_defeating_at_least_all_lakitu = 2035052211
        reach_the_goal_after_defeating_at_least_all_lemmy = 2038503215
        reach_the_goal_after_defeating_at_least_all_lava_bubble = 2048033177
        reach_the_goal_while_wearing_a_bullet_bill_mask = 2076496776
        reach_the_goal_as_big_mario = 2089161429
        reach_the_goal_as_cat_mario = 2111528319
        reach_the_goal_after_defeating_at_least_all_goomba_galoomba = 2131209407
        reach_the_goal_after_defeating_at_least_all_thwomp = 2139645066
        reach_the_goal_after_defeating_at_least_all_iggy = 2259346429
        reach_the_goal_while_wearing_a_dry_bones_shell = 2549654281
        reach_the_goal_after_defeating_at_least_all_sledge_bro = 2694559007
        reach_the_goal_after_defeating_at_least_all_rocky_wrench = 2746139466
        reach_the_goal_after_grabbing_at_least_all_50_coin = 2749601092
        reach_the_goal_as_flying_squirrel_mario = 2855236681
        reach_the_goal_as_buzzy_mario = 3036298571
        reach_the_goal_as_builder_mario = 3074433106
        reach_the_goal_as_cape_mario = 3146932243
        reach_the_goal_after_defeating_at_least_all_wendy = 3174413484
        reach_the_goal_while_wearing_a_cannon_box = 3206222275
        reach_the_goal_as_link = 3314955857
        reach_the_goal_while_you_have_super_star_invincibility = 3342591980
        reach_the_goal_after_defeating_at_least_all_goombrat_goombud = 3346433512
        reach_the_goal_after_grabbing_at_least_all_10_coin = 3348058176
        reach_the_goal_after_defeating_at_least_all_buzzy_beetle = 3353006607
        reach_the_goal_after_defeating_at_least_all_bowser_jr = 3392229961
        reach_the_goal_after_defeating_at_least_all_koopa_troopa = 3437308486
        reach_the_goal_after_defeating_at_least_all_chain_chomp = 3459144213
        reach_the_goal_after_defeating_at_least_all_muncher = 3466227835
        reach_the_goal_after_defeating_at_least_all_wiggler = 3481362698
        reach_the_goal_as_smb2_mario = 3513732174
        reach_the_goal_in_a_koopa_clown_car_junior_clown_car = 3649647177
        reach_the_goal_as_spiny_mario = 3725246406
        reach_the_goal_in_a_koopa_troopa_car = 3730243509
        reach_the_goal_after_defeating_at_least_all_piranha_plant_jumping_piranha_plant = 3748075486
        reach_the_goal_after_defeating_at_least_all_dry_bones = 3797704544
        reach_the_goal_after_defeating_at_least_all_stingby_stingbies = 3824561269
        reach_the_goal_after_defeating_at_least_all_piranha_creeper = 3833342952
        reach_the_goal_after_defeating_at_least_all_fire_piranha_plant = 3842179831
        reach_the_goal_after_breaking_at_least_all_crates = 3874680510
        reach_the_goal_after_defeating_at_least_all_ludwig = 3974581191
        reach_the_goal_as_super_mario = 3977257962
        reach_the_goal_after_defeating_at_least_all_skipsqueak = 4042480826
        reach_the_goal_after_grabbing_at_least_all_coin = 4116396131
        reach_the_goal_after_defeating_at_least_all_magikoopa = 4117878280
        reach_the_goal_after_grabbing_at_least_all_30_coin = 4122555074
        reach_the_goal_as_balloon_mario = 4153835197
        reach_the_goal_while_wearing_a_red_pow_box = 4172105156
        reach_the_goal_while_riding_yoshi = 4209535561
        reach_the_goal_after_defeating_at_least_all_spike_top = 4269094462
        reach_the_goal_after_defeating_at_least_all_banzai_bill = 4293354249

    class Gamestyle(IntEnum):
        smb1 = 12621
        smb3 = 13133
        nsmbw = 21847
        sm3dw = 22323
        smw = 22349

    class GameVersion(IntEnum):
        v1_0_0 = 0
        v1_0_1 = 1
        v1_1_0 = 2
        v2_0_0 = 3
        v3_0_0 = 4
        v3_0_1 = 5
        unk = 33

    class ClearConditionCategory(IntEnum):
        none = 0
        parts = 1
        status = 2
        actions = 3
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.start_y = self._io.read_u1()
        self.goal_y = self._io.read_u1()
        self.goal_x = self._io.read_s2le()
        self.timer = self._io.read_s2le()
        self.clear_condition_magnitude = self._io.read_s2le()
        self.year = self._io.read_s2le()
        self.month = self._io.read_s1()
        self.day = self._io.read_s1()
        self.hour = self._io.read_s1()
        self.minute = self._io.read_s1()
        self.autoscroll_speed = KaitaiStream.resolve_enum(Level.AutoscrollSpeed, self._io.read_u1())
        self.clear_condition_category = KaitaiStream.resolve_enum(Level.ClearConditionCategory, self._io.read_u1())
        self.clear_condition = KaitaiStream.resolve_enum(Level.ClearCondition, self._io.read_s4le())
        self.unk_gamever = self._io.read_s4le()
        self.unk_management_flags = self._io.read_s4le()
        self.clear_attempts = self._io.read_s4le()
        self.clear_time = self._io.read_s4le()
        self.unk_creation_id = self._io.read_u4le()
        self.unk_upload_id = self._io.read_s8le()
        self.game_version = KaitaiStream.resolve_enum(Level.GameVersion, self._io.read_s4le())
        self.unk1 = self._io.read_bytes(189)
        self.gamestyle = KaitaiStream.resolve_enum(Level.Gamestyle, self._io.read_s2le())
        self.unk2 = self._io.read_u1()
        self.name = (self._io.read_bytes(66)).decode(u"UTF-16LE")
        self.description = (self._io.read_bytes(202)).decode(u"UTF-16LE")
        self.overworld = Level.Map(self._io, self, self._root)
        self.subworld = Level.Map(self._io, self, self._root)

    class Map(KaitaiStruct):

        class BoundaryType(IntEnum):
            built_above_line = 0
            built_below_line = 1

        class AutoscrollType(IntEnum):
            none = 0
            slow = 1
            normal = 2
            fast = 3
            custom = 4

        class Orientation(IntEnum):
            horizontal = 0
            vertical = 1

        class Theme(IntEnum):
            overworld = 0
            underground = 1
            castle = 2
            airship = 3
            underwater = 4
            ghost_house = 5
            snow = 6
            desert = 7
            sky = 8
            forest = 9

        class LiquidMode(IntEnum):
            static = 0
            rising_or_falling = 1
            rising_and_falling = 2

        class LiquidSpeed(IntEnum):
            none = 0
            x1 = 1
            x2 = 2
            x3 = 3
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.theme = KaitaiStream.resolve_enum(Level.Map.Theme, self._io.read_u1())
            self.autoscroll_type = KaitaiStream.resolve_enum(Level.Map.AutoscrollType, self._io.read_u1())
            self.boundary_type = KaitaiStream.resolve_enum(Level.Map.BoundaryType, self._io.read_u1())
            self.orientation = KaitaiStream.resolve_enum(Level.Map.Orientation, self._io.read_u1())
            self.liquid_end_height = self._io.read_u1()
            self.liquid_mode = KaitaiStream.resolve_enum(Level.Map.LiquidMode, self._io.read_u1())
            self.liquid_speed = KaitaiStream.resolve_enum(Level.Map.LiquidSpeed, self._io.read_u1())
            self.liquid_start_height = self._io.read_u1()
            self.boundary_right = self._io.read_s4le()
            self.boundary_top = self._io.read_s4le()
            self.boundary_left = self._io.read_s4le()
            self.boundary_bottom = self._io.read_s4le()
            self.unk_flag = self._io.read_s4le()
            self.object_count = self._io.read_s4le()
            self.sound_effect_count = self._io.read_s4le()
            self.snake_block_count = self._io.read_s4le()
            self.clear_pipe_count = self._io.read_s4le()
            self.piranha_creeper_count = self._io.read_s4le()
            self.exclamation_mark_block_count = self._io.read_s4le()
            self.track_block_count = self._io.read_s4le()
            self.unk1 = self._io.read_s4le()
            self.ground_count = self._io.read_s4le()
            self.track_count = self._io.read_s4le()
            self.ice_count = self._io.read_s4le()
            self.objects = [None] * (2600)
            for i in range(2600):
                self.objects[i] = Level.Obj(self._io, self, self._root)

            self.sounds = [None] * (300)
            for i in range(300):
                self.sounds[i] = Level.Sound(self._io, self, self._root)

            self.snakes = [None] * (5)
            for i in range(5):
                self.snakes[i] = Level.Snake(self._io, self, self._root)

            self.clear_pipes = [None] * (200)
            for i in range(200):
                self.clear_pipes[i] = Level.ClearPipe(self._io, self, self._root)

            self.piranha_creepers = [None] * (10)
            for i in range(10):
                self.piranha_creepers[i] = Level.PiranhaCreeper(self._io, self, self._root)

            self.exclamation_blocks = [None] * (10)
            for i in range(10):
                self.exclamation_blocks[i] = Level.ExclamationBlock(self._io, self, self._root)

            self.track_blocks = [None] * (10)
            for i in range(10):
                self.track_blocks[i] = Level.TrackBlock(self._io, self, self._root)

            self.ground = [None] * (4000)
            for i in range(4000):
                self.ground[i] = Level.Ground(self._io, self, self._root)

            self.tracks = [None] * (1500)
            for i in range(1500):
                self.tracks[i] = Level.Track(self._io, self, self._root)

            self.icicles = [None] * (300)
            for i in range(300):
                self.icicles[i] = Level.Icicle(self._io, self, self._root)

            self.unk2 = self._io.read_bytes(3516)


    class ClearPipeNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = self._io.read_u1()
            self.index = self._io.read_u1()
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()
            self.width = self._io.read_u1()
            self.height = self._io.read_u1()
            self.unk1 = self._io.read_u1()
            self.direction = self._io.read_u1()


    class Track(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u2le()
            self.flags = self._io.read_u1()
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()
            self.type = self._io.read_u1()
            self.lid = self._io.read_u2le()
            self.unk2 = self._io.read_u2le()
            self.unk3 = self._io.read_u2le()


    class TrackBlockNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u1()
            self.direction = self._io.read_u1()
            self.unk2 = self._io.read_u2le()


    class Obj(KaitaiStruct):

        class ObjId(IntEnum):
            goomba = 0
            koopa = 1
            piranha_flower = 2
            hammer_bro = 3
            block = 4
            question_block = 5
            hard_block = 6
            ground = 7
            coin = 8
            pipe = 9
            spring = 10
            lift = 11
            thwomp = 12
            bullet_bill_blaster = 13
            mushroom_platform = 14
            bob_omb = 15
            semisolid_platform = 16
            bridge = 17
            p_switch = 18
            pow = 19
            super_mushroom = 20
            donut_block = 21
            cloud = 22
            note_block = 23
            fire_bar = 24
            spiny = 25
            goal_ground = 26
            goal = 27
            buzzy_beetle = 28
            hidden_block = 29
            lakitu = 30
            lakitu_cloud = 31
            banzai_bill = 32
            one_up = 33
            fire_flower = 34
            super_star = 35
            lava_lift = 36
            starting_brick = 37
            starting_arrow = 38
            magikoopa = 39
            spike_top = 40
            boo = 41
            clown_car = 42
            spikes = 43
            big_mushroom = 44
            shoe_goomba = 45
            dry_bones = 46
            cannon = 47
            blooper = 48
            castle_bridge = 49
            jumping_machine = 50
            skipsqueak = 51
            wiggler = 52
            fast_conveyor_belt = 53
            burner = 54
            door = 55
            cheep_cheep = 56
            muncher = 57
            rocky_wrench = 58
            track = 59
            lava_bubble = 60
            chain_chomp = 61
            bowser = 62
            ice_block = 63
            vine = 64
            stingby = 65
            arrow = 66
            one_way = 67
            saw = 68
            player = 69
            big_coin = 70
            half_collision_platform = 71
            koopa_car = 72
            cinobio = 73
            spike_ball = 74
            stone = 75
            twister = 76
            boom_boom = 77
            pokey = 78
            p_block = 79
            sprint_platform = 80
            smb2_mushroom = 81
            donut = 82
            skewer = 83
            snake_block = 84
            track_block = 85
            charvaargh = 86
            slight_slope = 87
            steep_slope = 88
            reel_camera = 89
            checkpoint_flag = 90
            seesaw = 91
            red_coin = 92
            clear_pipe = 93
            conveyor_belt = 94
            key = 95
            ant_trooper = 96
            warp_box = 97
            bowser_jr = 98
            on_off_block = 99
            dotted_line_block = 100
            water_marker = 101
            monty_mole = 102
            fish_bone = 103
            angry_sun = 104
            swinging_claw = 105
            tree = 106
            piranha_creeper = 107
            blinking_block = 108
            sound_effect = 109
            spike_block = 110
            mechakoopa = 111
            crate = 112
            mushroom_trampoline = 113
            porkupuffer = 114
            cinobic = 115
            super_hammer = 116
            bully = 117
            icicle = 118
            exclamation_block = 119
            lemmy = 120
            morton = 121
            larry = 122
            wendy = 123
            iggy = 124
            roy = 125
            ludwig = 126
            cannon_box = 127
            propeller_box = 128
            goomba_mask = 129
            bullet_bill_mask = 130
            red_pow_box = 131
            on_off_trampoline = 132
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s4le()
            self.y = self._io.read_s4le()
            self.unk1 = self._io.read_s2le()
            self.width = self._io.read_u1()
            self.height = self._io.read_u1()
            self.flag = self._io.read_s4le()
            self.cflag = self._io.read_s4le()
            self.ex = self._io.read_s4le()
            self.id = KaitaiStream.resolve_enum(Level.Obj.ObjId, self._io.read_s2le())
            self.cid = self._io.read_s2le()
            self.lid = self._io.read_s2le()
            self.sid = self._io.read_s2le()


    class Icicle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()
            self.type = self._io.read_u1()
            self.unk1 = self._io.read_u1()


    class Snake(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.index = self._io.read_u1()
            self.node_count = self._io.read_u1()
            self.unk1 = self._io.read_u2le()
            self.nodes = [None] * (120)
            for i in range(120):
                self.nodes[i] = Level.SnakeNode(self._io, self, self._root)



    class ClearPipe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.index = self._io.read_u1()
            self.node_count = self._io.read_u1()
            self.unk = self._io.read_u2le()
            self.nodes = [None] * (36)
            for i in range(36):
                self.nodes[i] = Level.ClearPipeNode(self._io, self, self._root)



    class ExclamationBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u1()
            self.index = self._io.read_u1()
            self.node_count = self._io.read_u1()
            self.unk2 = self._io.read_u1()
            self.nodes = [None] * (10)
            for i in range(10):
                self.nodes[i] = Level.ExclamationBlockNode(self._io, self, self._root)



    class Ground(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()
            self.id = self._io.read_u1()
            self.background_id = self._io.read_u1()


    class SnakeNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.index = self._io.read_u2le()
            self.direction = self._io.read_u2le()
            self.unk1 = self._io.read_u4le()


    class Sound(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = self._io.read_u1()
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()
            self.unk1 = self._io.read_u1()


    class TrackBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u1()
            self.index = self._io.read_u1()
            self.node_count = self._io.read_u1()
            self.unk2 = self._io.read_u1()
            self.nodes = [None] * (10)
            for i in range(10):
                self.nodes[i] = Level.TrackBlockNode(self._io, self, self._root)



    class PiranhaCreeperNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u1()
            self.direction = self._io.read_u1()
            self.unk2 = self._io.read_u2le()


    class PiranhaCreeper(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u1()
            self.index = self._io.read_u1()
            self.node_count = self._io.read_u1()
            self.unk2 = self._io.read_u1()
            self.nodes = [None] * (20)
            for i in range(20):
                self.nodes[i] = Level.PiranhaCreeperNode(self._io, self, self._root)



    class ExclamationBlockNode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u1()
            self.direction = self._io.read_u1()
            self.unk2 = self._io.read_u2le()



