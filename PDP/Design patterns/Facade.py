'''
The Facade Pattern is a structural design pattern that provides a simplified interface to a set of interfaces in a subsystem. 
It defines a higher-level interface that makes the subsystem easier to use, encapsulating its complexity. 
The Facade Pattern promotes loose coupling by hiding the intricate details of the subsystem and providing a unified interface for the client.

Key components of the Facade Pattern:

Facade: This is the class that provides a simplified, unified interface to the client. 
It delegates client requests to appropriate classes in the subsystem.

Subsystem Classes: These are the classes that make up the subsystem. 
They implement the functionality but may have complex interfaces that the client should not be directly exposed to.

Client: This is the class or code that interacts with the Facade to perform actions 
on the subsystem without needing to understand its internal details.
'''
# Subsystem Classes
class AudioPlayer:
    def play_audio(self, file):
        return f"Playing audio: {file}"


class VideoPlayer:
    def play_video(self, file):
        return f"Playing video: {file}"


class SubtitleManager:
    def add_subtitle(self, file, subtitle):
        return f"Adding subtitle '{subtitle}' to {file}"

# Facade


class MultimediaFacade:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.video_player = VideoPlayer()
        self.subtitle_manager = SubtitleManager()

    def play_multimedia(self, file, subtitle=None):
        result = []
        result.append(self.audio_player.play_audio(file))
        result.append(self.video_player.play_video(file))

        if subtitle:
            result.append(self.subtitle_manager.add_subtitle(file, subtitle))

        return result

# Client Code


def client_code(facade):
    return facade.play_multimedia("sample.mp4", subtitle="english.srt")


# Usage
multimedia_facade = MultimediaFacade()
result = client_code(multimedia_facade)

for operation_result in result:
    print(operation_result)
