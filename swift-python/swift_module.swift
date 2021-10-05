import Foundation

@_cdecl("add")
public func add (x: Int, y: Int) -> Int {
	return x+y
}

@_cdecl("strlen")
public func strlen (x: UnsafePointer<CChar>) -> Int{
    let s : String = "\(String(cString: x))"
    return s.count
}

@_cdecl("custom_function")
public func custom_function (x: UnsafePointer<CChar>) -> UnsafePointer<CChar>{
    let ret : String = "Hello \(String(cString: x))"
    return UnsafePointer<CChar>(ret)
}

@_cdecl("objc_autoreleaseReturnValue")
public func objc_autoreleaseReturnValue (x: Int) -> Int {
    return 0
}
