#-*- coding: utf-8 -*- 
from database import db_session, Work

def check_db():
    
    check = db_session.query(Work.id).distinct().all()
    
    if not check:
        
        import sqlite3
        
        conn = sqlite3.connect('works.db')
        c = conn.cursor()
        
        """ WORK """
        
        c.execute('''INSERT INTO WORK VALUES (1, "Демонтаж конструкций из лгк", "Демонтаж", 3.75, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (2, "Демонтаж бетонных перегородок", "Демонтаж", 25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (3, "Очистка от старой краски", "Демонтаж", 2.18, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (4, "Демонтаж вагонки", "Демонтаж", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (5, "Демонтаж цементнопесчанной стяжки до 100мм.", "Демонтаж", 12.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (6, "Демонтаж металлоконструкций", "Демонтаж", 375, "т")''')
        c.execute('''INSERT INTO WORK VALUES (7, "Устройство дверных проёмов в кирпичной стене(1/2 кирпича)", "Демонтаж", 37.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (8, "Устройство дверных проёмов в бетонной стене(до 200 мм.)", "Демонтаж", 75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (9, "Очистка от старой краски", "Демонтаж", 2.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (10, "Cнятие старых обоев", "Демонтаж", 1.625, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (11, "Сбивка старой штукатурки", "Демонтаж", 2.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (12, "Демонтаж керамической плитки", "Демонтаж", 3.75, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (13, "Разборка полов из ленолеума(ковролина)", "Демонтаж", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (14, "Разборка паркетного пола", "Демонтаж", 3.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (15, "Демонтаж дверного блока", "Демонтаж", 8.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (16, "Демонтаж оконного блока", "Демонтаж", 8.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (17, "Демонтаж ванны", "Демонтаж", 15, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (18, "Демонтаж труб", "Демонтаж", 1, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (19, "Демонтаж умывальника", "Демонтаж", 3.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (20, "Демонтаж унитаза", "Демонтаж", 3.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (21, "Разборка потолка армстронг", "Демонтаж", 2.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (22, "Демонтаж электропроводки", "Демонтаж", 1, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (23, "Демонтаж розеток и выключателей", "Демонтаж", 2, "шт")''')


        c.execute('''INSERT INTO WORK VALUES (24, "Цементнопесчанная стяжка до 50мм.", "Пол", 6.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (25, "Цементнопесчанная стяжка до 100мм.", "Пол", 8.75, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (26, "Самовыравнивающая стяжка", "Пол", 5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (27, "Керамзитобетонная стяжка", "Пол", 7.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (28, "Укладка бетона", "Пол", 20, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (29, "Армирование стяжки", "Пол", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (30, "Гидроизоляция", "Пол", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (31, "Наливные полы", "Пол", 12.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (32, "Теплые полы", "Пол", 6.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (33, "Ламинат", "Пол", 6.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (34, "Устройство фанеры или OSB на пол (в 1 слой)", "Пол", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (35, "Линолиум", "Пол", 3.75, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (36, "Ковролин", "Пол", 4.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (37, "Половая доска", "Пол", 2.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (38, "Паркет-доска", "Пол", 8.75, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (39, "Паркет", "Пол", 11.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (40, "Художественный паркет", "Пол", 14.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (41, "Шлифовка, лакировка пола", "Пол", 4.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (42, "Монтаж плинтусов пластиковых", "Пол", 2, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (43, "Монтаж плинтусов деревянных", "Пол", 3.75, "пм")''')

        
        c.execute('''INSERT INTO WORK VALUES (44, "Устройство перегородок кирпичных 120мм", "Стены", 7.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (45, "Устройство перегородок из пеноблоков", "Стены", 7.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (46, "Звукоизоляция стен минеральной ватой", "Стены", 1.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (47, "Устройство полистирольных плит на стены в один слой", "Стены", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (48, "Устройство полистирольных плит на стены в один слой в уровень", "Стены", 3.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (49, "Монтаж сетки штукатурной", "Стены", 1.875, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (50, "Монтаж уголка металического", "Стены", 1.5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (51, "Устройство штукатурки маячной до 30 мм", "Стены", 6.875, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (52, "Устройство перегородок из ЛГК", "Стены", 10, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (53, "Устройство фальшстен из ЛГК", "Стены", 6.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (54, "Монтаж ЛГК конструкций (2-слойная перегородка)", "Стены", 10, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (55, "Монтаж ЛГК конструкций (короб)", "Стены", 7.5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (56, "Устройство колон из ЛГК", "Стены", 10.625, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (57, "Заделка швов ЛГК конструкций", "Стены", 1.25, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (58, "Монтаж металического уголка, металической ленты", "Стены", 1.5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (59, "Поклейка малярной сетки на стены", "Стены", 1.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (60, "Штукатурка стен", "Стены", 6.875, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (61, "Грунтовка поверхности 1 слой", "Стены", 0.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (62, "Беспесчанка стен под обои или декоративную штукатурку", "Стены", 4.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (63, "Беспесчанка откосов до 300мм, под обои", "Стены", 15, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (64, "Беспесчанка стен под покраску", "Стены", 5.625, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (65, "Беспесчанка откосов до 300мм, под покраску", "Стены", 15, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (66, "Поклейка стекловолокна на стены", "Стены", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (67, "Поклейка стекловолокна на откосы до 300мм", "Стены", 2.5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (68, "Поклейка обоев под покраску на стены", "Стены", 4, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (69, "Поклейка обоев под покраску на откосы до 300мм", "Стены", 4, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (70, "Поклейка обоев без бодбора рисунка на стены", "Стены", 5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (71, "Поклейка обоев без подбора рисунка на откосы до 300мм", "Стены", 5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (72, "Поклейка обоев с подбором рисунка на стены", "Стены", 5.625, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (73, "Поклейка обоев с подбором рисунка на откосы до 300мм", "Стены", 5.625, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (74, "Покраска стен в/є краской", "Стены", 2.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (75, "Покраска многокомпонентная", "Стены", 5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (76, "Покраска откосов до 300мм, валиком 2 раза", "Стены", 4.375, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (77, "Устройство декоративной штукатурки на стенах", "Стены", 6.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (78, "Устройство декоративной штукатурки на откосы до 300мм", "Стены", 6.25, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (79, "Устройство венецианской штукатурки, короед", "Стены", 11.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (80, "Монтаж пластиковой вагонки на стены", "Стены", 6.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (81, "Монтаж деревянной вагонки на стены", "Стены", 9.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (82, "Вагонка мдф", "Стены", 5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (83, "Сайдинг", "Стены", 8.75, "м2")''')


        c.execute('''INSERT INTO WORK VALUES (84, "Устройство арок ГКЛ", "Проемы", 15, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (85, "Устройство откосов ГКЛ, окон и дверей (монтаж, выготовка, покраска)", "Проемы", 15, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (86, "Устройство полистирольных плит на откосы до 300мм, окон, дверей", "Проемы", 1.875, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (87, "Устройство маячной штукатурки откосов до 300мм, окон, дверей", "Проемы", 15, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (88, "Монтаж подоконников", "Проемы", 7.5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (89, "Монтаж обналичников и расширителей", "Проемы", 1.875, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (90, "Монтаж деревянных дверных блоков до 2 кв.м.", "Проемы", 31.25, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (91, "Врезка замков и фурнитуры", "Проемы", 12.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (92, "Установка окон", "Проемы", 25, "шт")''')


        c.execute('''INSERT INTO WORK VALUES (93, "Грунтовка поверхности 1 слой", "Потолок", 0.625, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (94, "Штукатурка потолка", "Потолок", 12.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (95, "Устройство ГКЛ конструкций (1 уровень)", "Потолок", 10, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (96, "Устройство прямых понижений потолков ГКЛ", "Потолок", 8.125, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (97, "Устройство радиусных (кривых) понижений потолков ГКЛ", "Потолок", 10, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (98, "Монтаж ГКЛ конструкций (короб)", "Потолок", 8.125, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (99, "Монтаж натяжных потолков", "Потолок", 11.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (100, "Устройство потолков 'Армстронг'", "Потолок", 5.625, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (101, "Поклейка сетки малярной на потолок", "Потолок", 2.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (102, "Беспесчанка потолков под обои", "Потолок", 4.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (103, "Беспесчанка потолков под покраску", "Потолок", 6.875, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (104, "Поклейка стекловолокна на потолок", "Потолок", 3.125, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (105, "Поклейка стекловолокна на понижение потолков", "Потолок", 3.125, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (106, "Поклейка обоев на потолок под покраску, без подбора рисунка", "Потолок", 5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (107, "Оклейка обоев шелк,нить,ткань", "Потолок", 6.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (108, "Покраска потолка", "Потолок", 4.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (109, "Поклейка багета декоративного до 50 мм", "Потолок", 3.25, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (110, "Шпаклевка и покраска декоративного багета до 50 мм", "Потолок", 1.25, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (111, "Багеты", "Потолок", 2, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (112, "Обшивка потолка деревянной вагонкой", "Потолок", 9.375, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (113, "Обшивка потолка пластиковой вагонкой", "Потолок", 6.25, "м2")''')

        c.execute('''INSERT INTO WORK VALUES (114, "Облицовка пола керамической плиткой", "Плитка", 12.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (115, "Облицовка стен керамической плиткой", "Плитка", 12.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (116, "Облицовка стен керамической плиткой размерами 100х100 мм.", "Плитка", 18.75, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (117, "Устройство керамического фриза до 100 мм.", "Плитка", 5.625, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (118, "Облицовка полов мрамором или гранитом", "Плитка", 21.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (119, "Облицовка полов художественной керамической плиткой", "Плитка", 17.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (120, "Облицовка стен мозаикой", "Плитка", 20, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (121, "Облицовка стен декоративной плиткой под 'кирпич' или камень'", "Плитка", 11.25, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (122, "Облицовка поверхности песчанником", "Плитка", 12.5, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (123, "Монтаж керамических плинтусов", "Плитка", 4.375, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (124, "Прирезка керамической плитки прямо", "Плитка", 1.875, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (125, "Прирезка керамической плитки радиусом / криволинейно", "Плитка", 3.75, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (126, "Затирка швов плитки", "Плитка", 0.625, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (127, "Затирка швов плитки под 'кирпич' или 'камень'", "Плитка", 2.75, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (128, "Прирезка камня", "Плитка", 3.75, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (129, "Монтаж плиточного декоративного уголка", "Плитка", 3.125, "пм")''')

        c.execute('''INSERT INTO WORK VALUES (130, "Монтаж эл.точек по кирпичу", "Электрика", 5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (131, "Монтаж эл.точек по бетону", "Электрика", 6.25, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (132, "Укладка эл.кабеля", "Электрика", 1, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (133, "Укладка гофры", "Электрика", 0.5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (134, "Укладка металлорукава", "Электрика", 0.625, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (135, "Укладка кабель-канала", "Электрика", 0.5, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (136, "Монтаж эл.щита", "Электрика", 50, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (137, "Заземление, громоотвод", "Электрика", 62.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (138, "Подключение к силовой электросети", "Электрика", 17.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (139, "Набор электрощита (монтаж автоматов)", "Электрика", 3.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (140, "Монтаж распределительных коробок и подрозетников", "Электрика", 1.875, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (141, "Монтаж, розеток и выключателей", "Электрика", 3.125, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (142, "Монтаж точечных светильников", "Электрика", 3.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (143, "Монтаж светильников бра", "Электрика", 7.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (144, "Монтаж люминисцентных светильников", "Электрика", 7.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (145, "Монтаж люстры", "Электрика", 18.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (146, "Монтаж и подключение входного звонка", "Электрика", 7.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (147, "Проектирование схемы силовой электропроводки с учетом нагрузок", "Электрика", 50, "шт")''')

        c.execute('''INSERT INTO WORK VALUES (148, "Укладка труб канализации", "Сантехника", 3.125, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (149, "Штробление под трубы", "Сантехника", 4.375, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (150, "Устройство выводов водоснабжения и отопления", "Сантехника", 25, "точка")''')
        c.execute('''INSERT INTO WORK VALUES (151, "Устройство выводов (кухня)", "Сантехника", 25, "компл")''')
        c.execute('''INSERT INTO WORK VALUES (152, "Устройство выводов (стиральная, посудомоечная машина)", "Сантехника", 25, "компл")''')
        c.execute('''INSERT INTO WORK VALUES (153, "Прокладка ПВХ трубы 50", "Сантехника", 3.125, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (154, "Прокладка ПВХ трубы 100", "Сантехника", 4.375, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (155, "Термоизоляция трубопровода", "Сантехника", 0.625, "пм")''')
        c.execute('''INSERT INTO WORK VALUES (156, "Монтаж счетчиков воды с обратным клапаном", "Сантехника", 20, "компл")''')
        c.execute('''INSERT INTO WORK VALUES (157, "Монтаж водозапорной арматуры", "Сантехника", 5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (158, "Монтаж фильтра грубой очистки", "Сантехника", 5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (159, "Монтаж фильтра тонкой очистки", "Сантехника", 8.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (160, "Монтаж люка ревизии", "Сантехника", 6.25, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (161, "Монтаж вентиляционной решетки", "Сантехника", 5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (162, "Комплектация отопительных радиаторов", "Сантехника", 10, "компл")''')
        c.execute('''INSERT INTO WORK VALUES (163, "Монтаж отопительных радиаторов", "Сантехника", 70, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (164, "Монтаж сантехнических аксессуаров", "Сантехника", 5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (165, "Монтаж умывальника", "Сантехника", 31.25, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (166, "Монтаж смесителя", "Сантехника", 7.5, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (167, "Монтаж сифона", "Сантехника", 3.75, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (168, "Монтаж полотенцесушителя", "Сантехника", 60, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (169, "Монтаж биде, унитаза на пол", "Сантехника", 50, "компл")''')
        c.execute('''INSERT INTO WORK VALUES (170, "Монтаж консольных биде, унитаза на раму (навесные)", "Сантехника", 100, "компл")''')
        c.execute('''INSERT INTO WORK VALUES (171, "Монтаж ванной", "Сантехника", 80, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (172, "Монтаж гидромассажной ванной", "Сантехника", 100, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (173, "Монтаж душевой кабины", "Сантехника", 50, "шт")''')
        c.execute('''INSERT INTO WORK VALUES (174, "Монтаж электробойлера", "Сантехника", 31.25, "шт")''')

        c.execute('''INSERT INTO WORK VALUES (175, "Фасовка строительного мусора в мешки", "Разное", 10.625, "м3")''')
        c.execute('''INSERT INTO WORK VALUES (176, "Спуск и загрузка строительного мусора на машину (лифт)", "Разное", 43.75, "машина")''')
        c.execute('''INSERT INTO WORK VALUES (177, "Вывоз строительного мусора", "Разное", 62.5, "машина")''')
        c.execute('''INSERT INTO WORK VALUES (178, "Вынос строительного мусора к мусоросборнику на улицу", "Разное", 7.5, "м3")''')
        c.execute('''INSERT INTO WORK VALUES (179, "Доставка строительных материалов", "Разное", 31.25, "машина")''')
        c.execute('''INSERT INTO WORK VALUES (180, "Разгрузка и подъем строительных материалов (лифт)", "Разное", 25, "машина")''')
        c.execute('''INSERT INTO WORK VALUES (181, "Рабочий проект", "Разное", 10, "м2")''')

        conn.commit()
check_db()

"""
        c.execute('''INSERT INTO WORK VALUES (4, "Плитка пол", "Плитка", 30, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (5, "Плитка стены", "Плитка", 30, "м2")''')
        c.execute('''INSERT INTO WORK VALUES (6, "Плитка фриз", "Плитка", 30, "м2")''')
        
"""


