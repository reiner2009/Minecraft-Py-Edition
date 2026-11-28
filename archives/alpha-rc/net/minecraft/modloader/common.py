class SubscribeEvent:
	def __init__(self, event_type):
		self.event_type=event_type
	def __call__(self, func):
		func.is_event_handler=True
		func.event_type=self.event_type
		return func
