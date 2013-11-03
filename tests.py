from annotations import AsClass, AsField
import unittest

class TestAnnotationsProcessLine(unittest.TestCase):
    def test_process_AsClass_normal(self):
        package, name = AsClass._process_annotation_line("#@(package=com.company.cool,name=Status) additional comment text")
        self.assertEqual("com.company.cool", package)
        self.assertEqual("Status", name)
        
    def test_process_AsClass_space(self):
        package, name = AsClass._process_annotation_line("#@(package=org.group.ngo, name=YippieSkippie) WEE$$$$@\/")
        self.assertEqual("org.group.ngo", package)
        self.assertEqual("YippieSkippie", name)
    
    def test_process_AsField_normal(self):
        name, type = AsField._process_annotation_line("#@(name=stringProp,type=String) some MOAR##comment")
        self.assertEqual("stringProp", name)
        self.assertEqual("String", type)
    
    def test_process_AsField_space(self):
        name, type = AsField._process_annotation_line("#@(name=some property name, type=com.weird.dude)")
        self.assertEqual("some property name", name)
        self.assertEqual("com.weird.dude", type)

if __name__ == '__main__':
    unittest.main()
