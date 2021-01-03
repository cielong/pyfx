class CollapsableMixin:
    """
    Mixins to collapse a tree.
    """

    def collapse(self):
        """
        Collapse the current node.
        """
        if not self.is_expanded():
            return
        self.toggle_expanded()

    def collapse_all(self):
        """
        Recursively collapse the current node and its children.
        """
        for child in self._children.values():
            if isinstance(child, CollapsableMixin):
                child.collapse_all()
        self.collapse()
