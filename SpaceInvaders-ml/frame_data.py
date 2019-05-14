class FrameData():
    '''
    A snapshot of game variables at a particular
    frame. Can be converted to a tensor for use
    in generating a predictive model that plays
    pong.
    '''
    def __init__(self, frame_no, input_opcode, player_coord, player_bullet, enemies, enemy_bullets, lives, score):
        '''
        input_opcode:
            0 = noop
            1 = move right
            2 = move left
            3 = shoot
        '''
        self.frame_no = frame_no
        self.input_opcode = input_opcode
        self.player_coord = player_coord
        self.player_bullet = player_bullet
        self.enemies = enemies
        self.enemy_bullets = enemy_bullets
        self.lives = lives
        self.score = score

    def to_tensor(self):
        arr = [[],[],[]]
        subList_size = 120

        arr[0].append(self.player_coord[0])
        arr[0].append(self.player_coord[1])

        player_bullet = (-1,-1)
        if self.player_bullet != None:
            player_bullet = (self.player_bullet[0], self.player_bullet[1])
        arr[0].append(player_bullet[0])
        arr[0].append(player_bullet[1])

        arr[0].append(self.lives)
        arr[0].append(self.score)

        for x in range(subList_size - len(arr[0])):
            arr[0].append(-1)

        for e in self.enemies:
            if e != None:
                arr.append(e[1])
                arr.append(e[2])

        for y in range(subList_size - len(arr[1])):
            arr[1].append(-1)


        for e_bullets in self.enemy_bullets:
            if e_bullets != None:
                arr[2].append(e_bullets[0])
                arr[2].append(e_bullets[1])

        for z in range(subList_size - len(arr[2])):
            arr[2].append(-1)


        #return [self.player_coord , self.player_bullet, self.enemies, self.enemy_bullets, self.barrier_particles, self.lives, self.score]

        return arr

    def to_processed_tensor(self):
        arr = [[],[],[]]
        subList_size = 120
        # The game field is (800, 600)
        arr[0].append(self.player_coord[0]/800)
        arr[0].append(self.player_coord[1]/600)


        player_bullet = (-1,-1)
        if self.player_bullet != None:
            player_bullet = (self.player_bullet[0]/800, self.player_bullet[1]/600)
        arr[0].append(player_bullet[0])
        arr[0].append(player_bullet[1])

        arr[0].append(self.lives/2)
        arr[0].append(self.score/10000)

        for x in range(subList_size - len(arr[0])):
            arr[0].append(-1)


        for e in self.enemies:
            if e != None:
                #enemies.append((e[0]/2, e[1]/800, e[2]/600))
                #continue
                #arr.append(e[0]/2)
                arr[1].append(e[1]/800)
                arr[1].append(e[2]/600)

        for y in range(subList_size - len(arr[1])):
            arr[1].append(-1)

        enemy_bullets = []
        for e_bullets in self.enemy_bullets:
            if e_bullets != None:
                arr[2].append(e_bullets[0]/800)
                arr[2].append(e_bullets[1]/600)

        for z in range(subList_size - len(arr[2])):
            arr[2].append(-1)

        #return [player_coord , player_bullet, enemies, enemy_bullets, barrier_particles, self.lives/2, self.score/10000]

        return arr

    def __str__(self):
        return "{} | {} | {} | {} | {} | {} | {} | {} | {}".format(self.frame_no, self.input_opcode, self.player_coord, self.player_bullet, self.enemies, self.enemy_bullets, self.barrier_particles, self.lives, self.score)
