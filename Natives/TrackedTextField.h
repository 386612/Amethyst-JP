#import <UIKit/UIKit.h>

#include "jni.h"

@interface TrackedTextField : UITextField

@property(nonatomic, copy) void(^sendChar)(jchar codepoint);
@property(nonatomic, copy) void(^sendCharMods)(jchar codepoint, int mods);
@property(nonatomic, copy) void(^sendKey)(int key, int scancode, int action, int mods);
// SDL/IME側の一時的なresign要求で標準キーボードが閉じるのを防ぐ。
// 明示的にキーボードボタンを押して閉じる場合だけNOにしてresignする。
@property(nonatomic, assign) BOOL preventUnexpectedResign;

@end
