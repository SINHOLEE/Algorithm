class Creature:
    HP = 0
    ATT = 0
    DEF = 0

    def attack(self, enemy):
        enemy.HP -= max(1, (self.ATT - enemy.DEF))


class Inventory:
    def __init__(self):
        self.weapon = 0
        self.armor = 0
        self.ornaments = []

    def find_ornament(self, name):
        for ornament in self.ornaments:
            if ornament.s == name:
                return True
        return False

    def del_ornament(self, name):
        for i in range(len(self.ornaments)):
            if self.ornaments[i].s == name:
                self.ornaments.pop(i)
                break


class Item:
    items = {}

    def __init__(self, r, c, t, s):
        self.r = r
        self.c = c
        self.t = t
        self.s = s
        Item.items[(self.r, self.c)] = self


class Monster(Creature):
    monsters = {}

    def __init__(self, r, c, name, w, a, h, e, isboss):
        self.r = r
        self.c = c
        self.name = name
        self.ATT = w
        self.DEF = a
        self.HP = h
        self.e = e
        self.isboss = isboss
        Monster.monsters[(self.r, self.c)] = self


class Character(Creature):
    def __init__(self, r, c):
        self.LEVEL = 1
        self.HP = 20
        self.s_att = 2
        self.s_def = 2
        self.EXP = 0
        self.NEXT_EXP = self.LEVEL * 5
        self.r = r
        self.c = c
        self.inventory = Inventory()
        self.ATT = self.s_att + self.inventory.weapon
        self.DEF = self.s_def + self.inventory.armor

    def co_attack(self, enemy):
        enemy.HP -= max(1, (2 * self.ATT - enemy.DEF))

    def co_dx_attack(self, enemy):
        enemy.HP -= max(1, (3 * self.ATT - enemy.DEF))

    def get_item(self, item):
        if item.t == 'W':
            self.inventory.weapon = int(item.s)
            self.ATT = int(item.s) + self.s_att
        elif item.t == 'A':
            self.inventory.armor = int(item.s)
            self.DEF = int(item.s) + self.s_def
        else:
            if len(self.inventory.ornaments) < 4 and not (self.inventory.find_ornament(item.s)):
                self.inventory.ornaments.append(item)

    def __repr__(self):
        return '''LV : %s
HP : %s/%s
ATT : %s+%s
DEF : %s+%s
EXP : %s/%s''' % (self.LEVEL, self.HP, 20 + (self.LEVEL-1)*5, self.s_att, self.inventory.weapon,\
       self.s_def, self.inventory.armor, self.EXP, self.NEXT_EXP)


n, m = map(int, input().split())

direction = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}
mat = [list(input()) for _ in range(n)]
move = list(input())
monsters_num = 0
items_num = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == '@':
            h_s_i = i
            h_s_j = j
            hero = Character(i, j)
            mat[i][j] = '.'
        if mat[i][j] == '&':
            monsters_num += 1
        if mat[i][j] == 'M':
            monsters_num += 1
            boss_r = i
            boss_c = j
        if mat[i][j] == 'B':
            items_num += 1

for _ in range(monsters_num):
    r, c, name, w, a, h, e = input().split()
    if mat[int(r)-1][int(c)-1] == 'M':
        Monster(int(r)-1, int(c)-1, name, int(w), int(a), int(h), int(e), True)
    else:
        Monster(int(r)-1, int(c)-1, name, int(w), int(a), int(h), int(e), False)
for _ in range(items_num):
    r, c, t, s = input().split()
    Item(int(r)-1, int(c)-1, t, s)


rnd = 0
for mov in move:
    rnd += 1

    ni, nj = hero.r + direction[mov][0], hero.c + direction[mov][1]
    if not (0 <= ni < n and 0 <= nj < m) or mat[ni][nj] == '#':
        ni, nj = hero.r, hero.c
    hero.r = ni
    hero.c = nj
    if mat[ni][nj] == '.':
        continue
    # 가시 밟으면 아파
    if mat[ni][nj] == '^':
        if hero.inventory.find_ornament('DX'):
            hero.HP -= 1
        else:
            hero.HP -= 5
        if hero.HP <= 0:
            if hero.inventory.find_ornament("RE"):
                hero.r = h_s_i
                hero.c = h_s_j
                hero.HP = 20 + (hero.LEVEL - 1) * 5
                hero.inventory.del_ornament('RE')
                continue
            for a in mat:
                print(''.join(a))
            print('Passed Turns :', rnd)
            hero.HP = 0
            print(hero)
            print("YOU HAVE BEEN KILLED BY SPIKE TRAP..")
            break
    # 몬스터 만나면 싸워
    if mat[ni][nj] == '&' or mat[ni][nj] == 'M':
        temp = Monster.monsters[(ni, nj)]
        monster_hp = temp.HP
        battle_rnd = 1
        if temp.isboss and hero.inventory.find_ornament('HU'):
            hero.HP = 20 + (hero.LEVEL-1) * 5
        while hero.HP > 0 and temp.HP > 0:

            if battle_rnd == 1 and hero.inventory.find_ornament('CO'):
                if hero.inventory.find_ornament('DX'):
                    hero.co_dx_attack(temp)
                else:
                    hero.co_attack(temp)
            else:
                hero.attack(temp)
            if temp.HP <= 0:
                break
            if temp.isboss and battle_rnd == 1 and hero.inventory.find_ornament('HU'):
                pass
            else:
                temp.attack(hero)
            battle_rnd += 1
        if hero.HP <= 0:
            if hero.inventory.find_ornament("RE"):
                hero.r = h_s_i
                hero.c = h_s_j
                hero.HP = 20 + (hero.LEVEL - 1) * 5
                hero.inventory.del_ornament('RE')
                temp.HP = monster_hp
                continue
            for a in mat:
                print(''.join(a))
            print('Passed Turns :', rnd)
            hero.HP = 0
            print(hero)
            print('YOU HAVE BEEN KILLED BY %s..' % temp.name)
            break
        else:
            if hero.inventory.find_ornament('EX'):
                hero.EXP += int(temp.e * 1.2)
            else:
                hero.EXP += temp.e
            if hero.inventory.find_ornament('HR'):
                hero.HP = min(hero.HP + 3, 20 + (hero.LEVEL-1) * 5)

            if hero.EXP >= hero.NEXT_EXP:
                hero.LEVEL += 1
                hero.HP = 20 + (hero.LEVEL - 1) * 5
                hero.s_att += 2
                hero.ATT += 2
                hero.s_def += 2
                hero.DEF += 2
                hero.NEXT_EXP += 5
                hero.EXP = 0
            mat[ni][nj] = '.'
            if temp.isboss:
                mat[hero.r][hero.c] = '@'
                for a in mat:
                    print(''.join(a))
                print('Passed Turns :', rnd)
                print(hero)
                print("YOU WIN!")
                break

    # 아이템 만나면 먹어
    if mat[ni][nj] == 'B':
        temp_item = Item.items[(ni, nj)]
        hero.get_item(temp_item)
        mat[ni][nj] = '.'

else:
    mat[hero.r][hero.c] = '@'
    for a in mat:
        print(''.join(a))
    print('Passed Turns :', rnd)
    print(hero)
    print('Press any key to continue.')