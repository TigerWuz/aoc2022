from utils.inputReader import InputReader

def day8_a():
    forest = InputReader.getDigits('input\\day8.txt')
    forest_rows     = len(forest)
    forest_columns  = len(forest[0])

    #The forest edges are already visible
    visible_trees   = (forest_rows * 2) + (forest_columns * 2) -4
    #check for each element the corresponding row and look
    #into every direction, n, e, s, w

    for row_index in range(1, forest_rows-1):
        for column_index in range(1, forest_columns-1):
            tree_is_visible = True
            current_tree_height = forest[row_index][column_index]
            compare_tree_height = 0
            
            #check northside, break if a tree is larger
            for i in range(row_index):
                compare_tree_height = forest[i][column_index]
                if current_tree_height <= compare_tree_height:
                    tree_is_visible = False
                    break
            
            #check southside
            if tree_is_visible == False:
                tree_is_visible = True
                for i in range(row_index+1,forest_rows):
                    compare_tree_height = forest[i][column_index]
                    if current_tree_height <= compare_tree_height:
                        tree_is_visible = False
                        break

            #check westside
            if tree_is_visible == False:
                tree_is_visible = True
                for i in range(column_index):
                    compare_tree_height = forest[row_index][i]
                    if current_tree_height <= compare_tree_height:
                        tree_is_visible = False
                        break
            
            #check eastside
            if tree_is_visible == False:
                tree_is_visible = True
                for i in range(column_index+1,forest_columns):
                    compare_tree_height = forest[row_index][i]
                    if current_tree_height <= compare_tree_height:
                        tree_is_visible = False
                        break

            if tree_is_visible == True:
                visible_trees += 1

    solution = visible_trees
    print('Day 8 Solution 1: {} Trees are visible.'.format(solution))

def day8_b():
    forest = InputReader.getDigits('input\\day8.txt')
    forest_rows     = len(forest)
    forest_columns  = len(forest[0])

    scenic_scores = []
    #check for each element the corresponding row and look
    #into every direction, n, e, s, w

    for row_index in range(forest_rows):
        for column_index in range(forest_columns):
            current_tree_scenic_score = [0, 0, 0, 0]
            current_tree_height = forest[row_index][column_index]
            compare_tree_height = 0
            
            #check northside, break if a tree is larger
            for i in range(row_index, 0, -1):
                compare_tree_height = forest[i-1][column_index]
                if current_tree_height <= compare_tree_height:
                    current_tree_scenic_score[0] += 1
                    break
                else:
                    current_tree_scenic_score[0] += 1
            
            #check southside
            for i in range(row_index+1,forest_rows):
                compare_tree_height = forest[i][column_index]
                if current_tree_height <= compare_tree_height:
                    current_tree_scenic_score[1] += 1
                    break
                else:
                    current_tree_scenic_score[1] += 1
                

            #check westside
            for i in range(column_index, 0, -1):
                compare_tree_height = forest[row_index][i-1]
                if current_tree_height <= compare_tree_height:
                    current_tree_scenic_score[2] += 1
                    break
                else:
                    current_tree_scenic_score[2] += 1
            
            #check eastside
            for i in range(column_index+1,forest_columns):
                compare_tree_height = forest[row_index][i]
                if current_tree_height <= compare_tree_height:
                    current_tree_scenic_score[3] += 1
                    break
                else:
                    current_tree_scenic_score[3] += 1

            score = current_tree_scenic_score[0] * current_tree_scenic_score[1] * current_tree_scenic_score[2] * current_tree_scenic_score[3]
            scenic_scores.append(score)

    solution = max(scenic_scores)
    print('Day 8 Solution 2s: Maximum scenic score is {}'.format(solution))

# day8_a()
day8_b()

