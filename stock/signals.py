from django import dispatch
stock_changed_signal = dispatch.Signal(["code","name","old_value","new_value"])