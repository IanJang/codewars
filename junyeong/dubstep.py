from junyeong import Test


def song_decoder(song):
    str = list(song.upper().replace("WUB", " ").lstrip().rstrip())
    for i, s in enumerate(str):
        if s == ' ' and str[i + 1] == ' ':
            str[i] = '.'
    return "".join(str).replace('.', '')
#
# def song_decoder2(song):
#
#     str = list(song.upper().replace("WUB", " ").lstrip().rstrip())
#     i = 0
#     while i < len(str):
#         if str[i] == ' ' and str[i + 1] == ' ':
#             del str[i]
#             i -= 1
#         i += 1
#     return "".join(str)
#
# def song_decoder3(song):
#     return ' '.join(song.replace('WUB', ' ').split(''))


def test_song_decoder():
    Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C", "WUB should be replaced by 1 space")
    Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C", "multiples WUB should be replaced by only 1 space")
    Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C", "heading or trailing spaces should be removed")

    Test.assert_equals(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"), "WE ARE THE CHAMPIONS MY FRIEND")
    Test.assert_equals(song_decoder("WUBWUBPWUBYWUBWUBTWUBHWUBWUBWUBOWUBNWUBWUB"), "P Y T H O N")
    Test.assert_equals(song_decoder("wUbAWUbbwubCwubwUB"), "A B C")
