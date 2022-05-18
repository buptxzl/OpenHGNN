import os
from dgl.data import DGLBuiltinDataset
from dgl.data.utils import load_graphs, save_graphs

__all__ = ['Amazon4GATNEDataset', 'Youtube4GATNEDataset', 'Twitter4GATNEDataset']


class _GATNEDataset(DGLBuiltinDataset):
    r"""GATNE Dataset.
    """

    def __init__(self, raw_dir=None, force_reload=False, verbose=False,
                 transform=None):
        pass

    def process(self):
        pass

    def save(self):
        graph_path = os.path.join(self.save_path, 'graph.bin')
        save_graphs(graph_path, self._g)

    def load(self):
        graph_path = os.path.join(self.save_path, 'graph.bin')
        gs, _ = load_graphs(graph_path)
        self._g = gs[0]

    def __getitem__(self, idx):
        assert idx == 0
        return self._g

    def __len__(self):
        return 1


class Amazon4GATNEDataset(_GATNEDataset):
    def __init__(self, raw_dir=None, force_reload=False, verbose=False, transform=None):
        name = 'amazon4GATNE'
        super(Amazon4GATNEDataset, self).__init__(name, raw_dir=raw_dir,
                                                  force_reload=force_reload, verbose=verbose, transform=transform)


class Youtube4GATNEDataset(_GATNEDataset):
    def __init__(self, raw_dir=None, force_reload=False, verbose=False, transform=None):
        name = 'youtube4GATNE'
        super(Youtube4GATNEDataset, self).__init__(name, raw_dir=raw_dir,
                                                   force_reload=force_reload, verbose=verbose, transform=transform)


class Twitter4GATNEDataset(_GATNEDataset):
    def __init__(self, raw_dir=None, force_reload=False, verbose=False, transform=None):
        name = 'twitter4GATNE'
        super(Twitter4GATNEDataset, self).__init__(name, raw_dir=raw_dir,
                                                   force_reload=force_reload, verbose=verbose, transform=transform)
