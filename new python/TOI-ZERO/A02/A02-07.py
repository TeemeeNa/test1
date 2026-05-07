import sys

def solve():
    # 1. เตรียมข้อมูล
    raw = sys.stdin.read().split()
    if not raw: return
    
    N, M = int(raw[0]), int(raw[1])
    buckets = []
    for i in range(N):
        # เก็บแค่ข้อมูลที่จำเป็น: ID, ขอบซ้าย(a), ขอบขวา(b)
        buckets.append({'id': i+1, 'a': int(raw[2+i*2]), 'b': int(raw[3+i*2]), 'children': [], 'is_target': False})
    
    # มาร์คว่าถังไหนคือถังที่เราต้องการ (เป้าหมาย)
    targets_start_idx = 2 + N * 2
    for i in range(M):
        target_id = int(raw[targets_start_idx + i])
        buckets[target_id - 1]['is_target'] = True

    # 2. สร้างโครงสร้าง "กล่องซ้อนกล่อง" (Tree)
    # ใครครอบใครอยู่? เราจะหา "พ่อ" ให้แต่ละถัง
    roots = []
    for i in range(N):
        parent = -1
        # หาถัง j ที่ครอบถัง i อยู่ และต้องเป็นถังที่ "เล็กที่สุด" ที่ครอบ i ได้
        for j in range(N):
            if i != j and buckets[j]['a'] < buckets[i]['a'] and buckets[j]['b'] > buckets[i]['b']:
                if parent == -1 or (buckets[j]['b'] - buckets[j]['a'] < buckets[parent]['b'] - buckets[parent]['a']):
                    parent = j
        
        if parent == -1: roots.append(i)
        else: buckets[parent]['children'].append(i)

    # 3. ฟังก์ชันตัดสินใจ (จะยก "ใบใหญ่ใบเดียว" หรือ "ใบเล็กหลายใบ" ดี?)
    def decide(u):
        # ข้อมูลพื้นฐานของกิ่งนี้
        my_id = buckets[u]['id']
        all_targets_inside = [my_id] if buckets[u]['is_target'] else []
        subtree_size = 1
        
        # ไปถามลูกๆ ก่อนว่าพวกเขามีทางเลือกยังไง
        child_picks = []
        for v in buckets[u]['children']:
            res = decide(v)
            child_picks.append(res)
            all_targets_inside.extend(res['targets'])
            subtree_size += res['size']

        # ถ้ากิ่งนี้ไม่มีเป้าหมายเลย ก็ไม่ต้องยกอะไรเลย
        if not all_targets_inside:
            return {'count': 0, 'waste': 0, 'list': [], 'targets': [], 'size': 1}

        # --- ทางเลือกที่ 1: ยกถังใบนี้ (u) ใบเดียวครอบคลุมทั้งหมด ---
        opt1_count = 1
        opt1_waste = subtree_size - len(all_targets_inside)
        opt1_list = [my_id]

        # --- ทางเลือกที่ 2: ไม่ยกใบนี้ แต่ให้ลูกๆ แยกกันยกกันเอง ---
        opt2_count = sum(c['count'] for c in child_picks)
        opt2_waste = sum(c['waste'] for c in child_picks)
        opt2_list = []
        for c in child_picks: opt2_list.extend(c['list'])

        # กฎพิเศษ: ถ้าตัวมันเอง (u) เป็นเป้าหมาย "ต้อง" เลือกวิธีที่เก็บตัวมันได้
        # ซึ่งในโครงสร้างนี้คือต้องยกใบนี้ (opt1) เท่านั้น เพราะไม่มีลูกคนไหนเก็บพ่อได้
        if buckets[u]['is_target']:
            return {'count': opt1_count, 'waste': opt1_waste, 'list': opt1_list, 'targets': all_targets_inside, 'size': subtree_size}

        # เปรียบเทียบ: 1.จำนวนถังน้อยกว่าชนะ 2.ถ้าเท่ากัน ถังแถมน้อยกว่าชนะ
        if opt1_count < opt2_count or (opt1_count == opt2_count and opt1_waste < opt2_waste):
            best = {'count': opt1_count, 'waste': opt1_waste, 'list': opt1_list}
        else:
            best = {'count': opt2_count, 'waste': opt2_waste, 'list': opt2_list}
            
        best.update({'targets': all_targets_inside, 'size': subtree_size})
        return best

    # 4. รวมคำตอบ
    final_list = []
    final_count = 0
    for r in roots:
        res = decide(r)
        final_count += res['count']
        final_list.extend(res['list'])

    print(final_count)
    print(*(sorted(final_list)))

solve()