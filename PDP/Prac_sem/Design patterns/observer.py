class User:
    def __init__(self, name):
        self.name = name

    def update(self, article, blog_writer):
        print(
            f'For {self.name}, new article {article} by {blog_writer.name} is added')


class BlogWriter:
    '''
    BlogWriter class is useful to blog writer to add new article
    and manage subscribers as well
    '''

    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.articles = []  # Article is the subject

    def add_article(self, article):
        '''
        Add new article and notify subscribers
        '''
        self.articles.append(article)
        self.notify_subscribers(article)

    def get_articles(self):
        '''
        Get articles written by {self}
        '''
        return self.articles

    def subscribe(self, subscriber):
        '''
        Add new subscriber to notify on adding article
        '''
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        '''
        User can unsubscribe from further notifications
        '''
        return self.subscribers.remove(subscriber)

    def subscribers(self):
        '''
        Get subsribers
        '''
        return self.subscribers

    def notify_subscribers(self, article):
        '''
        Notifying all the subsribers about new addition of an article
        '''
        for sub in self.subscribers:
            sub.update(article, self)


if __name__ == '__main__':
    blog_writer = BlogWriter('Hardik\'s blog')
    shailaja = User('Shailaja')
    aarav = User('Aarav')
    blog_writer.subscribe(shailaja)
    blog_writer.subscribe(aarav)
    blog_writer.add_article('Article 1')
    blog_writer.unsubscribe(aarav)
    blog_writer.add_article('Article 2')

# -------------------------------------------------------------------------------------------------
print("\n\n")


class Participants:
    def __init__(self, name):
        self.name = name

    def update(self, event_name, date, ieee_event):
        print(
            f'Hi {self.name}. A new event {event_name} is conducted by the IEEE {ieee_event.soceity_name} on {date}')


class IEEE_Events():
    def __init__(self, soceity_name):
        self.soceity_name = soceity_name
        self.__dates = []
        self.__participants = []
        self.__events = []

    def add_event(self, event_name, date):
        self. __events.append(event_name)
        self. __dates.append(date)
        self.alert_participants(event_name, date)

    def IEEE_MemParticipant(self, participant):
        self.__participants.append(participant)

    def IEEE_RemoveParticipant(self, participant):
        return self.__participants.remove(participant)

    def alert_participants(self, event_name, date):
        for participant in self.__participants:
            participant.update(event_name, date, self)

    def __str__(self):
        return self.__participants, self.__events, self.__dates


ieee_event = IEEE_Events('Computer Soceity')

participant1 = Participants('John')
participant2 = Participants('Jessy')

ieee_event.IEEE_MemParticipant(participant1)
ieee_event.IEEE_MemParticipant(participant2)

ieee_event.add_event('IEEEXtreme', '1-1-23')

ieee_event.IEEE_RemoveParticipant(participant2)

ieee_event.add_event('Guest Lecture Series', '2-1-23')

# print(ieee_event.__str__())
