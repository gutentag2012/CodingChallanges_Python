def translate(value, is_from, is_to, go_from, go_to):
    left_span = is_to - is_from
    right_span = go_to - go_from
    scale = float(value - is_from) / float(left_span)
    return go_from + (scale * right_span)
