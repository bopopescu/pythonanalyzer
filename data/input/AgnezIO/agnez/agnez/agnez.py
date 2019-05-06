# -*- coding: utf-8 -*-

class Masterpiece():
    """Masterpiece is a collection of arts and reports generated by the artists
    using information about the model and the dataset

    Parameters:
    ===========

    artists: list
        list of :class:`Artist` objects
    model: :class:`Model`
    dataset: :class:`Dataset`
    """
    def __init__(self, artists=None, model=None, dataset=None):
        self.model = model
        self.dataset = dataset
        self.artists = [a(model=model, dataset=dataset) for a in artists]

    def expose(self):
        """expose collects the arts from all the artists and publish them
        in the input media

        Paramters:
        =========
        media: :class:`Media`
            media object to render the resulting figures and texts
        """
        arts = [a.art() for a in self.artists]
        return arts


class IPythonNotebook(Masterpiece):
    """Media is a base class for that exposes all the art products. Examples
    of medias are IPython notebooks, html files, pdfs, etc
    """
    def __init__(self, *args, **kwargs):
        super(IPythonNotebook, self).__init__(*args, **kwargs)

    def expose(self):
        arts = super(IPythonNotebook, self).expose()
        self.nb = nbf.new_notebook()
        for art, artist in zip(arts, self.artists):
            cells += [nbf.new_title_cell(artist.header)]
            for viz, text in art:
                cells += nbf.new_code_cell(viz)
                cells += nbf.new_text_cell('markdown', text)
