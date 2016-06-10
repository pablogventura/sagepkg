#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Modulo con ejemplos rapidos, para hacer pruebas
"""

import fotheories

from model import FO_Model
from fotype import FO_Type
from fofunctions import FO_Relation, FO_Operation


tipoposet = FO_Type({}, {"<=": 2})
tiporet = FO_Type({"^": 2, "v": 2}, {})
tiporetacotado = FO_Type({"^": 2, "v": 2, "Max": 1, "Min": 1}, {})
tipotest = FO_Type({}, {"P": 1, "<=": 2})
tipodistinto = FO_Type({}, {"!=": 2})

posetrombo = FO_Model(tipoposet, range(4), {},
                      {'<=': FO_Relation({(0, 0): 1,
                                          (0, 1): 1,
                                          (0, 2): 1,
                                          (0, 3): 1,
                                          (1, 0): 0,
                                          (1, 1): 1,
                                          (1, 2): 0,
                                          (1, 3): 0,
                                          (2, 0): 0,
                                          (2, 1): 1,
                                          (2, 2): 1,
                                          (2, 3): 0,
                                          (3, 0): 0,
                                          (3, 1): 1,
                                          (3, 2): 0,
                                          (3, 3): 1}, range(4)), })

posetdiamante = FO_Model(tipoposet, range(5), {}, {"<=": FO_Relation({(0, 0): 1,
                                                                      (0, 1): 1,
                                                                      (0, 2): 1,
                                                                      (0, 3): 1,
                                                                      (0, 4): 1,
                                                                      (1, 0): 0,
                                                                      (1, 1): 1,
                                                                      (1, 2): 0,
                                                                      (1, 3): 0,
                                                                      (1, 4): 0,
                                                                      (2, 0): 0,
                                                                      (2, 1): 1,
                                                                      (2, 2): 1,
                                                                      (2, 3): 0,
                                                                      (2, 4): 0,
                                                                      (3, 0): 0,
                                                                      (3, 1): 1,
                                                                      (3, 2): 0,
                                                                      (3, 3): 1,
                                                                      (3, 4): 0,
                                                                      (4, 0): 0,
                                                                      (4, 1): 1,
                                                                      (4, 2): 0,
                                                                      (4, 3): 0,
                                                                      (4, 4): 1}, range(5))})

posetcadena2 = FO_Model(tipoposet, range(
    2), {}, {"<=": FO_Relation({(0, 0): 1, (0, 1): 0, (1, 0): 1, (1, 1): 1}, range(2))})

retdiamante = fotheories.Lat.find_models(5)[0]
rettestlinden = fotheories.DLat.find_models(7)[0]
retrombo = FO_Model(tiporetacotado, range(4), {'^': FO_Operation({(0, 0): 0,
                                                                  (0, 1): 0,
                                                                  (0, 2): 0,
                                                                  (0, 3): 0,
                                                                  (1, 0): 0,
                                                                  (1, 1): 1,
                                                                  (1, 2): 2,
                                                                  (1, 3): 3,
                                                                  (2, 0): 0,
                                                                  (2, 1): 2,
                                                                  (2, 2): 2,
                                                                  (2, 3): 0,
                                                                  (3, 0): 0,
                                                                  (3, 1): 3,
                                                                  (3, 2): 0,
                                                                  (3, 3): 3}),
                                               'v': FO_Operation({(0, 0): 0,
                                                                  (0, 1): 1,
                                                                  (0, 2): 2,
                                                                  (0, 3): 3,
                                                                  (1, 0): 1,
                                                                  (1, 1): 1,
                                                                  (1, 2): 1,
                                                                  (1, 3): 1,
                                                                  (2, 0): 2,
                                                                  (2, 1): 1,
                                                                  (2, 2): 2,
                                                                  (2, 3): 1,
                                                                  (3, 0): 3,
                                                                  (3, 1): 1,
                                                                  (3, 2): 1,
                                                                  (3, 3): 3}
                                                                 ),
                                               "Max": FO_Operation({(): 1}),
                                               "Min": FO_Operation({(): 0}),
                                               },
                    {'<=': FO_Relation({(0, 0): 1,
                                        (0, 1): 1,
                                        (0, 2): 1,
                                        (0, 3): 1,
                                        (1, 0): 0,
                                        (1, 1): 1,
                                        (1, 2): 0,
                                        (1, 3): 0,
                                        (2, 0): 0,
                                        (2, 1): 1,
                                        (2, 2): 1,
                                        (2, 3): 0,
                                        (3, 0): 0,
                                        (3, 1): 1,
                                        (3, 2): 0,
                                        (3, 3): 1}, range(4)),
                    '!=': FO_Relation({(0, 0): 0,
                                        (0, 1): 1,
                                        (0, 2): 1,
                                        (0, 3): 1,
                                        (1, 0): 1,
                                        (1, 1): 0,
                                        (1, 2): 1,
                                        (1, 3): 1,
                                        (2, 0): 1,
                                        (2, 1): 1,
                                        (2, 2): 0,
                                        (2, 3): 1,
                                        (3, 0): 1,
                                        (3, 1): 1,
                                        (3, 2): 1,
                                        (3, 3): 0}, range(4)),                                        
                     # Relacion de prueba
                     "P": FO_Relation({(0,): 0, (1,): 0, (2,): 1, (3,): 1}, range(4))
                     })

retrombo2 = FO_Model(tiporetacotado, [1, 2, 3, 4], {'^': FO_Operation({(1, 1): 1,
                                                                       (1, 2): 1,
                                                                       (1, 3): 1,
                                                                       (1, 4): 1,
                                                                       (2, 1): 1,
                                                                       (2, 2): 2,
                                                                       (2, 3): 3,
                                                                       (2, 4): 4,
                                                                       (3, 1): 1,
                                                                       (3, 2): 3,
                                                                       (3, 3): 3,
                                                                       (3, 4): 1,
                                                                       (4, 1): 1,
                                                                       (4, 2): 4,
                                                                       (4, 3): 1,
                                                                       (4, 4): 4}),
                                                    'v': FO_Operation({(1, 1): 1,
                                                                       (1, 2): 2,
                                                                       (1, 3): 3,
                                                                       (1, 4): 4,
                                                                       (2, 1): 2,
                                                                       (2, 2): 2,
                                                                       (2, 3): 2,
                                                                       (2, 4): 2,
                                                                       (3, 1): 3,
                                                                       (3, 2): 2,
                                                                       (3, 3): 3,
                                                                       (3, 4): 2,
                                                                       (4, 1): 4,
                                                                       (4, 2): 2,
                                                                       (4, 3): 2,
                                                                       (4, 4): 4}
                                                                      ),
                                                    "Max": FO_Operation({(): 2}),
                                                    "Min": FO_Operation({(): 1}),
                                                    },
                     {'<=': FO_Relation({(1, 1): 1,
                                         (1, 2): 1,
                                         (1, 3): 1,
                                         (1, 4): 1,
                                         (2, 1): 0,
                                         (2, 2): 1,
                                         (2, 3): 0,
                                         (2, 4): 0,
                                         (3, 1): 0,
                                         (3, 2): 1,
                                         (3, 3): 1,
                                         (3, 4): 0,
                                         (4, 1): 0,
                                         (4, 2): 1,
                                         (4, 3): 0,
                                         (4, 4): 1}, [1, 2, 3, 4]),
                      # Relacion de prueba
                      "P": FO_Relation({(1,): 0, (2,): 0, (3,): 1, (4,): 1}, [1, 2, 3, 4])
                      })


rettest10 = FO_Model(tiporet, range(10), {'^': FO_Operation([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 1, 2, 3, 4, 5,
     6, 7, 8, 9],
    [0, 2, 2, 0, 0, 0,
     0, 0, 0, 9],
    [0, 3, 0, 3, 0, 0,
     0, 0, 0, 9],
    [0, 4, 0, 0, 4, 0,
     0, 0, 0, 9],
    [0, 5, 0, 0, 0, 5,
     0, 0, 0, 9],
    [0, 6, 0, 0, 0, 0,
     6, 0, 0, 9],
    [0, 7, 0, 0, 0, 0,
     0, 7, 7, 9],
    [0, 8, 0, 0, 0, 0,
     0, 7, 8, 9],
    [9, 9, 9, 9, 9, 9,
     9, 9, 9, 9],
]),
    'v': FO_Operation([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 0],
        [1, 1, 1, 1, 1, 1,
         1, 1, 1, 1],
        [2, 1, 2, 1, 1, 1,
         1, 1, 1, 2],
        [3, 1, 1, 3, 1, 1,
         1, 1, 1, 3],
        [4, 1, 1, 1, 4, 1,
         1, 1, 1, 4],
        [5, 1, 1, 1, 1, 5,
         1, 1, 1, 5],
        [6, 1, 1, 1, 1, 1,
         6, 1, 1, 6],
        [7, 1, 1, 1, 1, 1,
         1, 7, 8, 7],
        [8, 1, 1, 1, 1, 1,
         1, 8, 8, 8],
        [0, 1, 2, 3, 4, 5,
         6, 7, 8, 9],
    ]),
},
    {})

rettest102 = FO_Model(tiporet,
                      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      {'v': FO_Operation({
                          (1, 1): 1,
                          (1, 2): 2,
                          (1, 3): 3,
                          (1, 4): 4,
                          (1, 5): 5,
                          (1, 6): 6,
                          (1, 7): 7,
                          (1, 8): 8,
                          (1, 9): 9,
                          (1, 10): 1,
                          (2, 1): 2,
                          (2, 2): 2,
                          (2, 3): 2,
                          (2, 4): 2,
                          (2, 5): 2,
                          (2, 6): 2,
                          (2, 7): 2,
                          (2, 8): 2,
                          (2, 9): 2,
                          (2, 10): 2,
                          (3, 1): 3,
                          (3, 2): 2,
                          (3, 3): 3,
                          (3, 4): 2,
                          (3, 5): 2,
                          (3, 6): 2,
                          (3, 7): 2,
                          (3, 8): 2,
                          (3, 9): 2,
                          (3, 10): 3,
                          (4, 1): 4,
                          (4, 2): 2,
                          (4, 3): 2,
                          (4, 4): 4,
                          (4, 5): 2,
                          (4, 6): 2,
                          (4, 7): 2,
                          (4, 8): 2,
                          (4, 9): 2,
                          (4, 10): 4,
                          (5, 1): 5,
                          (5, 2): 2,
                          (5, 3): 2,
                          (5, 4): 2,
                          (5, 5): 5,
                          (5, 6): 2,
                          (5, 7): 2,
                          (5, 8): 2,
                          (5, 9): 2,
                          (5, 10): 5,
                          (6, 1): 6,
                          (6, 2): 2,
                          (6, 3): 2,
                          (6, 4): 2,
                          (6, 5): 2,
                          (6, 6): 6,
                          (6, 7): 2,
                          (6, 8): 2,
                          (6, 9): 2,
                          (6, 10): 6,
                          (7, 1): 7,
                          (7, 2): 2,
                          (7, 3): 2,
                          (7, 4): 2,
                          (7, 5): 2,
                          (7, 6): 2,
                          (7, 7): 7,
                          (7, 8): 2,
                          (7, 9): 2,
                          (7, 10): 7,
                          (8, 1): 8,
                          (8, 2): 2,
                          (8, 3): 2,
                          (8, 4): 2,
                          (8, 5): 2,
                          (8, 6): 2,
                          (8, 7): 2,
                          (8, 8): 8,
                          (8, 9): 9,
                          (8, 10): 8,
                          (9, 1): 9,
                          (9, 2): 2,
                          (9, 3): 2,
                          (9, 4): 2,
                          (9, 5): 2,
                          (9, 6): 2,
                          (9, 7): 2,
                          (9, 8): 9,
                          (9, 9): 9,
                          (9, 10): 9,
                          (10, 1): 1,
                          (10, 2): 2,
                          (10, 3): 3,
                          (10, 4): 4,
                          (10, 5): 5,
                          (10, 6): 6,
                          (10, 7): 7,
                          (10, 8): 8,
                          (10, 9): 9,
                          (10, 10): 10, }
                      ), '^': FO_Operation({
                          (1, 1): 1,
                          (1, 2): 1,
                          (1, 3): 1,
                          (1, 4): 1,
                          (1, 5): 1,
                          (1, 6): 1,
                          (1, 7): 1,
                          (1, 8): 1,
                          (1, 9): 1,
                          (1, 10): 10,
                          (2, 1): 1,
                          (2, 2): 2,
                          (2, 3): 3,
                          (2, 4): 4,
                          (2, 5): 5,
                          (2, 6): 6,
                          (2, 7): 7,
                          (2, 8): 8,
                          (2, 9): 9,
                          (2, 10): 10,
                          (3, 1): 1,
                          (3, 2): 3,
                          (3, 3): 3,
                          (3, 4): 1,
                          (3, 5): 1,
                          (3, 6): 1,
                          (3, 7): 1,
                          (3, 8): 1,
                          (3, 9): 1,
                          (3, 10): 10,
                          (4, 1): 1,
                          (4, 2): 4,
                          (4, 3): 1,
                          (4, 4): 4,
                          (4, 5): 1,
                          (4, 6): 1,
                          (4, 7): 1,
                          (4, 8): 1,
                          (4, 9): 1,
                          (4, 10): 10,
                          (5, 1): 1,
                          (5, 2): 5,
                          (5, 3): 1,
                          (5, 4): 1,
                          (5, 5): 5,
                          (5, 6): 1,
                          (5, 7): 1,
                          (5, 8): 1,
                          (5, 9): 1,
                          (5, 10): 10,
                          (6, 1): 1,
                          (6, 2): 6,
                          (6, 3): 1,
                          (6, 4): 1,
                          (6, 5): 1,
                          (6, 6): 6,
                          (6, 7): 1,
                          (6, 8): 1,
                          (6, 9): 1,
                          (6, 10): 10,
                          (7, 1): 1,
                          (7, 2): 7,
                          (7, 3): 1,
                          (7, 4): 1,
                          (7, 5): 1,
                          (7, 6): 1,
                          (7, 7): 7,
                          (7, 8): 1,
                          (7, 9): 1,
                          (7, 10): 10,
                          (8, 1): 1,
                          (8, 2): 8,
                          (8, 3): 1,
                          (8, 4): 1,
                          (8, 5): 1,
                          (8, 6): 1,
                          (8, 7): 1,
                          (8, 8): 8,
                          (8, 9): 8,
                          (8, 10): 10,
                          (9, 1): 1,
                          (9, 2): 9,
                          (9, 3): 1,
                          (9, 4): 1,
                          (9, 5): 1,
                          (9, 6): 1,
                          (9, 7): 1,
                          (9, 8): 8,
                          (9, 9): 9,
                          (9, 10): 10,
                          (10, 1): 10,
                          (10, 2): 10,
                          (10, 3): 10,
                          (10, 4): 10,
                          (10, 5): 10,
                          (10, 6): 10,
                          (10, 7): 10,
                          (10, 8): 10,
                          (10, 9): 10,
                          (10, 10): 10,
                      })},
                      {}
                      )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
