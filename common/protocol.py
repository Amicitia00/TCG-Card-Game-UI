from enum import Enum
from enum import Enum


class CustomProtocol(Enum):
    ACCOUNT_REGISTER = 1
    ACCOUNT_LOGIN = 2

    SESSION_LOGIN = 3

    BATTLE_WAIT_QUEUE_FOR_MATCH = 11
    BATTLE_READY = 12
    CANCEL_MATCH = 13 #13
    CHECK_BATTLE_PREPARE = 14 #14
    WHAT_IS_THE_ROOM_NUMBER = 15 #15
    BATTLE_DECK_LIST = 16 #16
    BATTLE_START_SHUFFLED_GAME_DECK_CARD_LIST = 17 #17
    CHANGE_FIRST_HAND = 18

    ACCOUNT_CARD_LIST = 31
    ACCOUNT_DECK_REGISTER = 41

    SHOP_DATA = 71
    SHOP_GACHA = 72
    FREE_GACHA = 73
    EVENT_DISTRIBUTE_CARDS = 90

    MULLIGAN_CARD = 1012


    USE_UNIT_CARD = 1004
    USE_ITEM_CARD = 1005
    USE_TRAP_CARD = 1006
    USE_TOOL_CARD = 1007
    USE_ENVIRONMENT_CARD = 1008
    USE_SUPPORT_CARD = 1009
    USE_ENERGY_CARD = 1010
    USE_SPECIAL_ENERGY_CARD = 1011

    DRAW_CARD_BY_SUPPORT_CARD = 1013

    UNIT_ATTACK = 1021
    UNIT_FIRST_SKILL = 1022
    UNIT_SECOND_SKILL = 1023

    TURN_END = 3333
    SURRENDER = 4443
    PROGRAM_EXIT = 4444

    CREATE_FAKE_BATTLE_ROOM = 8001



