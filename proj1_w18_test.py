import unittest
import proj1_w18 as proj1

class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince", "1982")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.releaseYear, "0")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.releaseYear, "1982")

    def testSongConstructor(self):

        s1 = proj1.Song()
        s2 = proj1.Song("Love Scars", "Trippie Redd", "2017", "A Love Letter To You", "Rap", "144")

        self.assertEqual(s1.title, "No Title")
        self.assertEqual(s1.author, "No Author")
        self.assertEqual(s1.length, "0")
        self.assertEqual(s1.album, "No Album Title")
        self.assertEqual(s1.genre, "No Genre")
        self.assertEqual(s1.releaseYear, "2000")

        self.assertEqual(s2.title, "Love Scars")
        self.assertEqual(s2.author, "Trippie Redd")
        self.assertEqual(s2.length, "144")
        self.assertEqual(s2.album, "A Love Letter To You")
        self.assertEqual(s2.genre, "Rap")
        self.assertEqual(s2.releaseYear, "2017")

    def testMovieConstructor(self):

        m1 = proj1.Movie()
        m2 = proj1.Movie("Inception", "Christopher Nolan", "2010", "PG13", "148")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.releaseYear, "2000")
        self.assertEqual(m1.rating, "G")
        self.assertEqual(m1.length, "100")

        self.assertEqual(m2.title, "Inception")
        self.assertEqual(m2.author, "Christopher Nolan")
        self.assertEqual(m2.releaseYear, "2010")
        self.assertEqual(m2.rating, "PG13")
        self.assertEqual(m2.length, "148")

    def testStr(self):

        m1 = proj1.Media("TR666", "Trippie Redd", "2018")
        s1 = proj1.Song("Love Scars", "Trippie Redd", "2017", "A Love Letter To You", "Rap", "144")
        m2 = proj1.Movie("Inception", "Christopher Nolan", "2010", "PG13", "148")

        test1 = m1.__str__()
        self.assertEqual(test1, "TR666 by Trippie Redd (2018)")

        test2 = s1.__str__()
        self.assertEqual(test2, "Love Scars by Trippie Redd (2017) [Rap]")

        test3 = m2.__str__()
        self.assertEqual(test3, "Inception by Christopher Nolan (2010) [PG13]")

    def testLen(self):

        m1 = proj1.Media("TR666", "Trippie Redd", "2018")
        s1 = proj1.Song("Love Scars", "Trippie Redd", "2017", "A Love Letter To You", "Rap", "144")
        s2 = proj1.Song()
        m2 = proj1.Movie("Inception", "Christopher Nolan", "2010", "PG13", "148")
        m3 = proj1.Movie()

        test1 = m1.__len__()
        self.assertEqual(test1, "0")

        test2 = s1.__len__()
        self.assertEqual(test2, "144")

        test3 = s2.__len__()
        self.assertEqual(test3, "0")

        test4 = m2.__len__()
        self.assertEqual(test4, "148")

        test5 = m3.__len__()
        self.assertEqual(test5, "100")

    def tetsInstanceVariables(self):

        m1 = proj1.Media("TR666", "Trippie Redd", "2018")
        s1 = proj1.Song("Love Scars", "Trippie Redd", "2017", "A Love Letter To You", "Rap", "144")
        m2 = proj1.Movie("Inception", "Christopher Nolan", "2010", "PG13", "148")

################################################################################
########################    Media   ############################################
################################################################################
        try:
            length1 = m1.length
            test1 = "failed"
        except:
            test1 = "passed"
        self.assertEqual(test1, "passed")

        try:
            rating1 = m1.rating
            test2 = "failed"
        except:
            test2 = "passed"
        self.assertEqual(test2, "passed")

        try:
            genre1 = m1.genre
            test3 = "failed"
        except:
            test3 = "passed"
        self.assertEqual(test3, "passed")

        try:
            album1 = m1.album
            test4 = "failed"
        except:
            test4 = "passed"
        self.assertEqual(test4, "passed")

################################################################################
########################    Song    ############################################
################################################################################
        try:
            rating1 = s1.rating
            test5 = "failed"
        except:
            test5 = "passed"
        self.assertEqual(test5, "passed")

################################################################################
########################    Movie   ############################################
################################################################################

        try:
            album1 = m2.album
            test6 = "failed"
        except:
            test6 = "passed"
        self.assertEqual(test6, "passed")

        try:
            genre1 = m2.genre
            test7 = "failed"
        except:
            test7 = "passed"
        self.assertEqual(test7, "passed")


class TestJsonClasses(unittest.TestCase):

    def testMediaJsonConstructor(self):

        json1 = {"wrapperType": "audiobook", "artistId": 2082069, "collectionId": 516799841, "artistName": "Helen Fielding", "collectionName": "Bridget Jones's Diary (Unabridged)", "collectionCensoredName": "Bridget Jones's Diary (Unabridged)", "artistViewUrl": "https://itunes.apple.com/us/author/helen-fielding/id2082069?mt=11&uo=4", "collectionViewUrl": "https://itunes.apple.com/us/audiobook/bridget-joness-diary-unabridged/id516799841?uo=4", "artworkUrl60": "http://is4.mzstatic.com/image/thumb/Music/v4/23/5f/08/235f0893-fe39-452a-0b2e-f1fb173fa82a/source/60x60bb.jpg", "artworkUrl100": "http://is4.mzstatic.com/image/thumb/Music/v4/23/5f/08/235f0893-fe39-452a-0b2e-f1fb173fa82a/source/100x100bb.jpg", "collectionPrice": 20.95, "collectionExplicitness": "notExplicit", "trackCount": 1, "copyright": "\u2117 \u00a9 2012 Recorded Books", "country": "USA", "currency": "USD", "releaseDate": "2012-04-03T07:00:00Z", "primaryGenreName": "Fiction", "previewUrl": "https://audio-ssl.itunes.apple.com/apple-assets-us-std-000001/Music7/v4/d4/bc/c8/d4bcc89b-d66e-e015-2c3e-3f6432ccffa0/mzaf_51579112983128144.plus.aac.p.m4a", "description": "<i>\"Sunday1 January: 129 lbs. (but post-Christmas), alcohol units 14 (but effectively covers 2 days as 4 hours of party was on New Year's Day), cigarettes 22, calories 5424.\"</i> <br /><br />From its beginning as a weekly column in a British newspaper, <i>Bridget Jones's Diary</i> quickly became a best-seller in England. After gaining international popularity, it also shot to the top of the <i>New York Times</i> best-seller list. A 30-something single professional, Bridget Jones prefers a diary to a day planner for tracking her life. Each entry is an honest and hilarious step in her endless quest for self-improvement. (\"New Year's Resolution: Go to gym three times a week not merely to buy sandwich.\") Caught between match-making relatives, other singles, and smug marrieds, Bridget records the triumphs and faux-pas of her life in this diary. <br /><br />Funny, witty, and, at times, charmingly innocent, <i>Bridget Jones's Diary</i> has a voice that is absolutely authentic. You've seen the Bridgets of the world trot by on their way to the office or gym. Now, through Barbara Rosenblat's narration, you'll spend some wonderful hours in the company of one. But be warned: from the very first line, you'll be laughing out loud and looking for friends to introduce to this wonderful young woman."}

        m1 = proj1.Media(json = json1)

        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.releaseYear, "2012")

        m1Str = m1.__str__()
        test1 = "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)"
        self.assertEqual(m1Str, test1)

        m1Len = m1.__len__()
        test2 = "0"
        self.assertEqual(m1Len, test2)

    def testSongJsonConstructor(self):

        json2 = {"wrapperType": "track", "kind": "song", "artistId": 136975, "collectionId": 400835735, "trackId": 400835962, "artistName": "The Beatles", "collectionName": "TheBeatles 1967-1970 (The Blue Album)", "trackName": "Hey Jude", "collectionCensoredName": "The Beatles 1967-1970 (The Blue Album)", "trackCensoredName": "Hey Jude", "artistViewUrl": "https://itunes.apple.com/us/artist/the-beatles/136975?uo=4", "collectionViewUrl": "https://itunes.apple.com/us/album/hey-jude/400835735?i=400835962&uo=4", "trackViewUrl": "https://itunes.apple.com/us/album/hey-jude/400835735?i=400835962&uo=4", "previewUrl": "https://audio-ssl.itunes.apple.com/apple-assets-us-std-000001/Music/v4/d5/c8/10/d5c81035-a242-c354-45cf-f634e4127f43/mzaf_1171292596660883824.plus.aac.p.m4a", "artworkUrl30": "http://is3.mzstatic.com/image/thumb/Music/v4/63/ac/ef/63acef5a-8b6a-b748-5d4c-e6a7e9c13c37/source/30x30bb.jpg", "artworkUrl60": "http://is3.mzstatic.com/image/thumb/Music/v4/63/ac/ef/63acef5a-8b6a-b748-5d4c-e6a7e9c13c37/source/60x60bb.jpg", "artworkUrl100": "http://is3.mzstatic.com/image/thumb/Music/v4/63/ac/ef/63acef5a-8b6a-b748-5d4c-e6a7e9c13c37/source/100x100bb.jpg", "collectionPrice": 19.99, "trackPrice": 1.29, "releaseDate": "1968-08-26T07:00:00Z", "collectionExplicitness": "notExplicit", "trackExplicitness": "notExplicit", "discCount": 2, "discNumber": 1, "trackCount": 14, "trackNumber": 13, "trackTimeMillis": 431333, "country": "USA", "currency": "USD", "primaryGenreName": "Rock", "isStreamable": "true"}

        s1 = proj1.Song(json = json2)

        self.assertEqual(s1.album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(s1.genre, "Rock")
        self.assertEqual(s1.length, "431")
        self.assertEqual(s1.title, "Hey Jude")
        self.assertEqual(s1.author, "The Beatles")
        self.assertEqual(s1.releaseYear, "1968")

        s1Str = s1.__str__()
        test1 = "Hey Jude by The Beatles (1968) [Rock]"
        self.assertEqual(s1Str, test1)

        s1Len = s1.__len__()
        test2 = "431"
        self.assertEqual(s1Len, test2)

    def testMovieJsonConstructor(self):

        json3 = {"wrapperType": "track", "kind": "feature-movie", "collectionId": 949030693, "trackId": 526768967, "artistName": "Steven Spielberg", "collectionName": "Steven Spielberg 7-Movie Director\u2019s Collection", "trackName": "Jaws", "collectionCensoredName": "Steven Spielberg 7-Movie Director\u2019s Collection", "trackCensoredName": "Jaws", "collectionArtistId": 345353262, "collectionArtistViewUrl": "https://itunes.apple.com/us/artist/universal-studios-home-entertainment/345353262?uo=4", "collectionViewUrl": "https://itunes.apple.com/us/movie/jaws/id526768967?uo=4", "trackViewUrl": "https://itunes.apple.com/us/movie/jaws/id526768967?uo=4", "previewUrl": "http://video.itunes.apple.com/apple-assets-us-std-000001/Video127/v4/a5/4c/6d/a54c6d2c-7003-1ae7-f002-84b4444bc05b/mzvf_5104399247891878253.640x266.h264lc.U.p.m4v", "artworkUrl30": "http://is1.mzstatic.com/image/thumb/Video18/v4/3c/ce/31/3cce31a9-ff9e-bc6b-f17d-a20c55d50db0/source/30x30bb.jpg", "artworkUrl60": "http://is1.mzstatic.com/image/thumb/Video18/v4/3c/ce/31/3cce31a9-ff9e-bc6b-f17d-a20c55d50db0/source/60x60bb.jpg", "artworkUrl100": "http://is1.mzstatic.com/image/thumb/Video18/v4/3c/ce/31/3cce31a9-ff9e-bc6b-f17d-a20c55d50db0/source/100x100bb.jpg", "collectionPrice": 9.99, "trackPrice": 9.99, "trackRentalPrice": 3.99, "collectionHdPrice": 14.99, "trackHdPrice": 14.99, "trackHdRentalPrice": 3.99, "releaseDate": "1975-06-20T07:00:00Z", "collectionExplicitness": "notExplicit", "trackExplicitness": "notExplicit", "discCount": 1, "discNumber": 1, "trackCount": 7, "trackNumber": 4, "trackTimeMillis": 7451455, "country": "USA", "currency": "USD", "primaryGenreName": "Thriller", "contentAdvisoryRating": "PG", "longDescription": "Directed by Academy Award\u00ae winner Steven Spielberg, Jaws set the standard for edge-of-your seat suspense, quickly becoming a cultural phenomenon and forever changing the way audiences experience movies. When the seaside community of Amityfinds itself under attack by a dangerous great white shark, the town\u2019s chief of police (Roy Scheider), a young marine biologist (Richard Dreyfuss) and a grizzled shark hunter (Robert Shaw) embark on a desperate quest to destroy the beast before it strikes again. Featuring an unforgettable score that evokes pure terror, Jaws remains one of the most influential and gripping adventures in motion picture history."}

        m1 = proj1.Movie(json = json3)

        self.assertEqual(m1.rating, "PG")
        self.assertEqual(m1.length, "124")
        self.assertEqual(m1.title, "Jaws")
        self.assertEqual(m1.author, "Steven Spielberg")
        self.assertEqual(m1.releaseYear, "1975")

        m1Str = m1.__str__()
        test1 = "Jaws by Steven Spielberg (1975) [PG]"
        self.assertEqual(m1Str, test1)

        m1Len = m1.__len__()
        test2 = "124"
        self.assertEqual(m1Len, test2)

class testItunesAPI(unittest.TestCase):

    def testMediaAPI(self):
        objects = proj1.apiCall("Banana Pancakes")
        self.assertEqual(len(objects), 38)

    def testSongAPI(self):
        objects = proj1.apiCall("Jack Johnson")
        self.assertEqual(len(objects), 50)

    def testMovieAPI(self):
        objects = proj1.apiCall("Shawshank Redemption")
        self.assertEqual(len(objects), 50)

    def testEmptyCall(self):
        objects = proj1.apiCall("")
        self.assertEqual(len(objects), 0)

    def testEmptyCall2(self):
        objects = proj1.apiCall(" ")
        self.assertEqual(len(objects), 0)

    def testNoResults(self):
        objects = proj1.apiCall("hklasmndfjkhhjkasdbmn,f")
        self.assertEqual(len(objects), 0)

    def testCommonWord(self):
        objects = proj1.apiCall("friend")
        self.assertEqual(len(objects), 50)

    def testCommonWord2(self):
        objects = proj1.apiCall("love")
        self.assertEqual(len(objects), 50)

    def testLessCommonWord(self):
        objects = proj1.apiCall("Moana")
        self.assertEqual(len(objects), 1)

    def testLessCommonWord(self):
        objects = proj1.apiCall("Moana")
        self.assertEqual(len(objects), 50)

    def testLessCommonWord2(self):
        objects = proj1.apiCall("Kris Wu")
        self.assertEqual(len(objects), 17)

    def testLessCommonWord3(self):
        objects = proj1.apiCall("Kent Jones")
        self.assertEqual(len(objects), 49)

unittest.main()
