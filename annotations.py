import re

class AsClass:
    def __init__(self, annotation_line):
        self.annotation_line = annotation_line
        self.package, self.name = self._process_annotation_line(annotation_line)
        self.children = []
    
    @staticmethod
    def _process_annotation_line(annotation_line):
        #@(package=...,name=...)
        pattern = re.compile(r'@\(package=(?P<package>.*),.*name=(?P<name>.*)\)')
        match = pattern.search(annotation_line)
        if match is None:
            return None, None
        return match.group('package'), match.group('name')
    
    def add_child(self, as_field):
        if isinstance(as_field, AsField):
            self.children.append(as_field)

class AsField:
    def __init__(self, annotation_line):
        self.annotation_line = annotation_line
        self.name, self.type = self._process_annotation_line(annotation_line)
    
    @staticmethod
    def _process_annotation_line(annotation_line):
        #@(name=...,type=...)
        pattern = re.compile(r'@\(name=(?P<name>.*),.*type=(?P<type>.*)\)')
        match = pattern.search(annotation_line)
        if match is None:
            return None, None
        return match.group('name'), match.group('type')
