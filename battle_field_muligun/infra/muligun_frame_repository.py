from battle_field_muligun.state.current_hand import CurrentHandState
from opengl_battle_field_pickable_card.legacy.pickable_card import LegacyPickableCard
from opengl_battle_field_pickable_card.pickable_card import PickableCard


class MuligunFrameRepository:
    __instance = None

    is_opponent_mulligan_done = False
    is_my_mulligan_done = False
    is_doing_mulligan = True
    is_reshape_not_complete = True
    timer_visible = True
    ok_button_visible = True
    ok_button_clicked = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance


    def set_is_opponent_mulligan(self, mulligan_done):
        self.is_opponent_mulligan_done = mulligan_done

    def get_is_opponent_mulligan(self):
        return self.is_opponent_mulligan_done

    def set_is_my_mulligan(self, mulligan_done):
        self.is_my_mulligan_done = mulligan_done

    def get_is_my_mulligan(self):
        return self.is_my_mulligan_done

    def set_is_doing_mulligan(self, is_doing_mulligan):
        self.is_doing_mulligan = is_doing_mulligan

    def get_is_doing_mulligan(self):
        return self.is_doing_mulligan

    def set_is_reshape_not_complete(self, is_reshape_not_complete):
        self.is_reshape_not_complete = is_reshape_not_complete

    def get_is_reshape_not_complete(self):
        return self.is_reshape_not_complete

    def set_timer_visible(self, timer_visible):
        self.timer_visible = timer_visible

    def get_timer_visible(self):
        return self.timer_visible

    def set_ok_button_visible(self, ok_button_visible):
        self.ok_button_visible = ok_button_visible

    def get_ok_button_visible(self):
        return self.ok_button_visible

    def set_ok_button_clicked(self, ok_button_clicked):
        self.ok_button_clicked = ok_button_clicked

    def get_ok_button_clicked(self):
        return self.ok_button_clicked

    def saveTransmitIpcChannel(self, transmitIpcChannel):
        print("BattleFieldMeligunFrameRepositoryImpl: saveTransmitIpcChannel()")
        self.__transmitIpcChannel = transmitIpcChannel

    def saveReceiveIpcChannel(self, receiveIpcChannel):
        print("BattleFieldMeligunFrameRepositoryImpl: saveReceiveIpcChannel()")
        self.__receiveIpcChannel = receiveIpcChannel
