def grade(arg, flag):
    if 'ytplayer.config.args.url_encoded_fmt_stream_map' in flag:
        return True, 'You seem to stream your way around'
    else:
        return False, 'Incorrect'
