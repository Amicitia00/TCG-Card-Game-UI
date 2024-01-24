from lobby_frame.entity.lobby_menu_frame import LobbyMenuFrame
from lobby_frame.repository.lobby_menu_frame_repository import LobbyMenuFrameRepository


class LobbyMenuFrameRepositoryImpl(LobbyMenuFrameRepository):
    __instance = None
    __receiveIpcChannel = None
    __transmitIpcChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createLobbyMenuFrame(self, rootWindow):
        print("MainMenuFrameRepositoryImpl: createLobbyMenuFrame()")
        lobbyMenuFrame = LobbyMenuFrame(rootWindow)

        return lobbyMenuFrame

    def requestDeckNameList(self, deckNameRequest):
        self.__transmitIpcChannel.put(deckNameRequest)
        return self.__receiveIpcChannel.get()

        # print(f"lobby_manu_frame Error")
        # result = [{"deckName" : "이거되나"},
        #           {"deckName" : "ㅋㅋㅋㅋㅋㅋ"},
        #           {"deckName": "오제발"},
        #           {"deckName": "안되면망함"}
        # ]
        # return result

    def startMatch(self, startMatchingRequest):
        self.__transmitIpcChannel.put(startMatchingRequest)
        return self.__receiveIpcChannel.get()

    def checkMatching(self, checkMatchingRequest):
        self.__transmitIpcChannel.put(checkMatchingRequest)
        return self.__receiveIpcChannel.get()

    def saveReceiveIpcChannel(self, receiveIpcChannel):
        self.__receiveIpcChannel = receiveIpcChannel

    def saveTransmitIpcChannel(self, transmitIpcChannel):
        self.__transmitIpcChannel = transmitIpcChannel

