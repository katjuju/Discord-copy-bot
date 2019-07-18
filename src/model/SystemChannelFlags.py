class SystemChannelFlags:

    def __init__(self):
        self.join_notifications = None;
        self.premium_subscriptions = None;


    def fillFromSystemChannelFlags(self, systemChannelFlags):
        self.join_notifications = systemChannelFlags.join_notifications;
        self.premium_subscriptions = systemChannelFlags.premium_subscriptions;
