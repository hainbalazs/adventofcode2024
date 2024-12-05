import networkx as nx

with open('input.txt') as f:
    input_lines = f.readlines()

DG = nx.DiGraph()
section = 'rules'
records = []
for line in input_lines:
    if section == 'rules':
        if '|' in line: 
            lt, gt = line.strip().split('|')
            DG.add_edge(int(lt), int(gt))
        else:
            section = 'ordering'
    else:
        records.append(line.strip().split(','))

acc = 0
for record in records:
    assert len(record) % 2 == 1
    record = [int(r) for r in record]

    subgraph = DG.subgraph([r for r in record if r in DG.nodes])
    if nx.is_directed_acyclic_graph(subgraph):
        order = list(nx.topological_sort(subgraph))
        if order == record:
            acc += record[(len(record) // 2)]
    else:
        print(f"Cycle detected in update: {record}")
        assert()

print(acc)