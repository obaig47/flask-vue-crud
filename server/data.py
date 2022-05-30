"""
data.py

Declares EVENTS constant -> 50 rows of mockaroo data with python uuid generated to
support dynamic ID assignment and referencing of ID's to update and delete records
"""

import uuid

EVENTS = [
  {
  'id': uuid.uuid4().hex,
    "title": "Thérèse: The Story of Saint Thérèse of Lisieux",
    "image": "http://dummyimage.com/485x365.png/ff4444/ffffff",
    "date": "2021-10-25",
    "time": "14:21"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Death of a Cyclist (Muerte de un ciclista)",
    "image": "http://dummyimage.com/489x612.png/cc0000/ffffff",
    "date": "2022-03-10",
    "time": "17:20"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "King of Comedy (Hei kek ji wong)",
    "image": "http://dummyimage.com/961x121.png/dddddd/000000",
    "date": "2022-04-11",
    "time": "18:53"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Mongolian Ping-Pong (Lü cao di)",
    "image": "http://dummyimage.com/887x554.png/ff4444/ffffff",
    "date": "2022-04-16",
    "time": "15:20"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Get Carter",
    "image": "http://dummyimage.com/314x548.png/5fa2dd/ffffff",
    "date": "2022-05-05",
    "time": "22:31"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Assault on Precinct 13",
    "image": "http://dummyimage.com/111x745.png/ff4444/ffffff",
    "date": "2022-04-28",
    "time": "20:12"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Resurrection, A",
    "image": "http://dummyimage.com/557x488.png/cc0000/ffffff",
    "date": "2021-10-09",
    "time": "1:48"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Kaena: The Prophecy (Kaena: La prophétie)",
    "image": "http://dummyimage.com/331x930.png/ff4444/ffffff",
    "date": "2021-07-03",
    "time": "14:07"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Last Remake of Beau Geste, The",
    "image": "http://dummyimage.com/759x103.png/5fa2dd/ffffff",
    "date": "2021-12-26",
    "time": "3:42"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "House That Dripped Blood, The",
    "image": "http://dummyimage.com/895x897.png/5fa2dd/ffffff",
    "date": "2022-05-09",
    "time": "17:26"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Executive Target",
    "image": "http://dummyimage.com/297x864.png/dddddd/000000",
    "date": "2022-03-10",
    "time": "11:08"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Mujhse Shaadi Karogi",
    "image": "http://dummyimage.com/442x736.png/ff4444/ffffff",
    "date": "2021-07-25",
    "time": "1:01"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Day Without a Mexican, A",
    "image": "http://dummyimage.com/246x822.png/ff4444/ffffff",
    "date": "2022-01-15",
    "time": "10:27"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Art of Dying, The (El Arte de Morir)",
    "image": "http://dummyimage.com/864x979.png/cc0000/ffffff",
    "date": "2021-09-21",
    "time": "15:57"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Mean Season, The",
    "image": "http://dummyimage.com/142x454.png/cc0000/ffffff",
    "date": "2021-09-22",
    "time": "19:58"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Christopher Strong",
    "image": "http://dummyimage.com/368x659.png/5fa2dd/ffffff",
    "date": "2021-11-19",
    "time": "7:25"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Mighty, The",
    "image": "http://dummyimage.com/883x940.png/dddddd/000000",
    "date": "2021-11-19",
    "time": "23:05"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Stuck",
    "image": "http://dummyimage.com/235x360.png/5fa2dd/ffffff",
    "date": "2021-09-05",
    "time": "1:06"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Savage Messiah",
    "image": "http://dummyimage.com/590x296.png/cc0000/ffffff",
    "date": "2021-12-12",
    "time": "22:01"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "A Promise",
    "image": "http://dummyimage.com/898x517.png/5fa2dd/ffffff",
    "date": "2022-05-13",
    "time": "0:04"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Ike: Countdown to D-Day",
    "image": "http://dummyimage.com/852x900.png/ff4444/ffffff",
    "date": "2021-09-08",
    "time": "1:44"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "One Piece Film: Strong World",
    "image": "http://dummyimage.com/560x488.png/dddddd/000000",
    "date": "2021-07-24",
    "time": "6:10"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Griff the Invisible",
    "image": "http://dummyimage.com/330x876.png/cc0000/ffffff",
    "date": "2022-05-14",
    "time": "10:27"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "DOA: Dead or Alive",
    "image": "http://dummyimage.com/273x514.png/dddddd/000000",
    "date": "2022-04-10",
    "time": "8:46"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Turner & Hooch",
    "image": "http://dummyimage.com/478x229.png/cc0000/ffffff",
    "date": "2021-10-20",
    "time": "7:35"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Mister Roberts",
    "image": "http://dummyimage.com/480x623.png/ff4444/ffffff",
    "date": "2022-01-09",
    "time": "18:52"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Freeway II: Confessions of a Trickbaby",
    "image": "http://dummyimage.com/520x490.png/ff4444/ffffff",
    "date": "2022-04-11",
    "time": "12:38"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Epitaph",
    "image": "http://dummyimage.com/247x878.png/5fa2dd/ffffff",
    "date": "2021-08-10",
    "time": "16:51"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Good Man in Africa, A",
    "image": "http://dummyimage.com/972x793.png/cc0000/ffffff",
    "date": "2022-03-18",
    "time": "13:07"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Mack, The",
    "image": "http://dummyimage.com/436x888.png/dddddd/000000",
    "date": "2022-03-18",
    "time": "19:51"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Maya Lin: A Strong Clear Vision",
    "image": "http://dummyimage.com/793x976.png/5fa2dd/ffffff",
    "date": "2021-10-25",
    "time": "9:29"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "On the Silver Globe (Na srebrnym globie)",
    "image": "http://dummyimage.com/291x789.png/5fa2dd/ffffff",
    "date": "2022-05-03",
    "time": "3:07"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Extreme Days",
    "image": "http://dummyimage.com/750x389.png/dddddd/000000",
    "date": "2021-09-20",
    "time": "13:21"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Amigo",
    "image": "http://dummyimage.com/334x663.png/dddddd/000000",
    "date": "2021-11-23",
    "time": "2:51"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Bey Yaar",
    "image": "http://dummyimage.com/691x946.png/dddddd/000000",
    "date": "2021-11-24",
    "time": "0:53"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Bound for Glory",
    "image": "http://dummyimage.com/489x393.png/5fa2dd/ffffff",
    "date": "2021-06-25",
    "time": "18:36"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Sunshine on Leith",
    "image": "http://dummyimage.com/594x799.png/ff4444/ffffff",
    "date": "2021-11-04",
    "time": "7:05"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Big Green, The",
    "image": "http://dummyimage.com/256x992.png/ff4444/ffffff",
    "date": "2021-08-25",
    "time": "18:18"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Monty Python and the Holy Grail",
    "image": "http://dummyimage.com/450x837.png/dddddd/000000",
    "date": "2022-03-15",
    "time": "3:45"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Cliffhanger",
    "image": "http://dummyimage.com/813x415.png/dddddd/000000",
    "date": "2021-09-28",
    "time": "6:08"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "From Dusk Till Dawn 3: The Hangman's Daughter",
    "image": "http://dummyimage.com/758x312.png/ff4444/ffffff",
    "date": "2022-03-19",
    "time": "12:38"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "The Beautiful Story",
    "image": "http://dummyimage.com/800x766.png/cc0000/ffffff",
    "date": "2022-01-06",
    "time": "18:10"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Crawling Hand, The",
    "image": "http://dummyimage.com/721x215.png/ff4444/ffffff",
    "date": "2022-03-28",
    "time": "21:32"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Star Trek Into Darkness",
    "image": "http://dummyimage.com/833x487.png/dddddd/000000",
    "date": "2022-05-21",
    "time": "2:03"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Cruel Romance, A (Zhestokij Romans)",
    "image": "http://dummyimage.com/959x575.png/cc0000/ffffff",
    "date": "2021-10-06",
    "time": "1:54"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Bit by Bit",
    "image": "http://dummyimage.com/331x691.png/5fa2dd/ffffff",
    "date": "2021-06-12",
    "time": "14:55"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Iron Man: Rise Of Technovore",
    "image": "http://dummyimage.com/231x435.png/ff4444/ffffff",
    "date": "2021-08-09",
    "time": "9:57"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Less of Sugar (Cheeni Kum)",
    "image": "http://dummyimage.com/698x240.png/cc0000/ffffff",
    "date": "2021-06-11",
    "time": "8:38"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "Phantom Carriage, The (Körkarlen)",
    "image": "http://dummyimage.com/783x274.png/5fa2dd/ffffff",
    "date": "2021-08-03",
    "time": "22:41"
  },
  {
  'id': uuid.uuid4().hex,
    "title": "In Praise of Love (Éloge de l'amour)",
    "image": "http://dummyimage.com/406x539.png/cc0000/ffffff",
    "date": "2021-12-07",
    "time": "4:03"
  }
]
